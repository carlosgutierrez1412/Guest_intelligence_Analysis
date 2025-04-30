import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os

st.cache_data.clear()


st.write("📂 Current directory:", os.getcwd())
st.write("📄 Contents of views folder:", os.listdir(BASE_PATH))


st.set_page_config(page_title="Guest Intelligence Dashboard", layout="wide")
st.title("Guest Intelligence Dashboard \U0001f4ca")

BASE_PATH = Path(__file__).resolve().parent.parent / "views"


@st.cache_data
def load_csv(file_name):
    return pd.read_csv(BASE_PATH / file_name, header=0)


# Load CSVs
df_daily = load_csv("vw_daily_revenue.csv")
df_items = load_csv("vw_sales_by_item.csv")
df_time = load_csv("vw_sales_by_time_of_day.csv")
df_type = load_csv("vw_sales_by_item_type.csv")
df_tx = load_csv("vw_transaction_type_breakdown.csv")
df_top_items = load_csv("vw_top_items_per_type.csv")
df_tiers = load_csv("vw_order_tiers.csv")
df_time_perf = load_csv("vw_daily_time_performance.csv")

for df in [
    df_daily,
    df_items,
    df_time,
    df_type,
    df_tx,
    df_top_items,
    df_tiers,
    df_time_perf,
]:
    df.columns = [col.strip().lower() for col in df.columns]


if "date" in df_time_perf.columns:
    df_daily["date"] = pd.to_datetime(df_daily["date"])
    df_time_perf["date"] = pd.to_datetime(df_time_perf["date"])
else:
    st.error("❌ 'date' column missing in df_time_perf — check data structure.")
    st.stop()

st.subheader("\U0001f4ca Key Performance Indicators")
k1, k2, k3 = st.columns(3)
k1.metric("Total Revenue", f"${df_daily['total_revenue'].sum():,.0f}")
k2.metric("Total Units Sold", f"{df_daily['total_units_sold'].sum():,}")
k3.metric("Total Days", f"{df_daily['date'].nunique()}")

df_monthly = df_daily.copy()
df_monthly["month"] = df_monthly["date"].dt.to_period("M").dt.to_timestamp()
df_monthly = df_monthly.groupby("month", as_index=False)["total_revenue"].sum()
st.subheader("\U0001f4c8 Monthly Revenue Trend")
fig1 = px.line(df_monthly, x="month", y="total_revenue", title="Revenue Over Time")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("\U0001f947 Top 10 Selling Items")
fig2 = px.bar(
    df_items.head(10),
    x="item_name",
    y="total_units_sold",
    title="Top Items by Quantity",
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("\U0001fa06 Revenue by Item Type")
fig3 = px.bar(
    df_type,
    x="total_revenue",
    y="item_type",
    orientation="h",
    title="Revenue by Category",
)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("\U0001f552 Revenue by Time of Day")
fig4 = px.pie(
    df_time,
    names="time_of_sale",
    values="total_revenue",
    title="Time-of-Day Sales Share",
)
st.plotly_chart(fig4, use_container_width=True)

if not df_tx.empty:
    st.subheader("\U0001f4cb Transaction Type Breakdown")
    fig5 = px.bar(
        df_tx,
        x="transaction_type",
        y="total_revenue",
        title="Revenue by Transaction Type",
    )
    st.plotly_chart(fig5, use_container_width=True)

st.subheader("\U0001f3f7️ Order Revenue Tier Distribution")
tier_counts = df_tiers["revenue_tier"].value_counts().reset_index()
tier_counts.columns = ["tier", "count"]
fig6 = px.pie(tier_counts, names="tier", values="count", title="Order Tiers")
st.plotly_chart(fig6, use_container_width=True)

st.subheader("⭐ Top 3 Items by Type")
st.dataframe(df_top_items)

st.subheader("\U0001f4ca Revenue Heatmap: Time of Day vs. Month")
df_time_perf["month"] = df_time_perf["date"].dt.to_period("M").dt.to_timestamp()
heatmap_df = (
    df_time_perf.groupby(["time_of_sale", "month"])["revenue"].sum().reset_index()
)
heatmap_pivot = heatmap_df.pivot(
    index="time_of_sale", columns="month", values="revenue"
)
time_order = ["Morning", "Afternoon", "Evening", "Night"]
heatmap_pivot = heatmap_pivot.reindex(time_order)
fig_heatmap = px.imshow(
    heatmap_pivot,
    labels=dict(x="Month", y="Time of Sale", color="Revenue"),
    color_continuous_scale="blues",
    aspect="auto",
)
fig_heatmap.update_traces(
    hovertemplate="Time: %{y}<br>Month: %{x|%b %Y}<br>Revenue: $%{z:,.2f}<extra></extra>"
)
st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("---")
st.caption(
    "Built with \U0001f4bb by Carlos Gutierrez | Powered by CSVs + Streamlit + Plotly"
)
