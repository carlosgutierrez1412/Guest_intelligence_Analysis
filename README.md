# Guest Intelligence Dashboard 📊

An interactive analytics dashboard built with **SQL**, **Pyhton**, **Excel**, **Streamlit**, **Pandas**, and **Plotly** to visualize guest behavior and sales performance from a public dataset on **Kaggle** (https://www.kaggle.com/datasets/rajatsurana979/fast-food-sales-report). This project aligns with the role of a **Guest Intelligence Analyst** by analyzing customer data, identifying trends, and presenting insights in a usable interface.

---

## 🌐 Live Demo
[Try the Dashboard on Streamlit Cloud](https://guestintelligenceanalysis-h6jjpeg6eyrn79zfbzuacu.streamlit.app/) 

---

## 🔍 Key Features
- **SQL Views**: Data was pre-processed and aggregated using SQL Server, then exported as CSVs
- **Powerful Visuals**: Interactive KPIs, bar charts, pie charts, and a monthly heatmap
- **Cloud-Deployable**: Hosted on [Streamlit Cloud](https://streamlit.io/cloud)
- **Modular Codebase**: Organized by data view for easy updates or expansion

---

## ⚙️ Tools & Technologies
- **SQL Server**:
  - Designed and created **8 SQL views** to clean, transform, and aggregate raw transactional data.
  - Used:
    - `SELECT`, `FROM`, `WHERE`, and `JOIN` statements to merge sales and item dimensions
    - `GROUP BY`, `ORDER BY`, and `COUNT`/`SUM` for aggregation logic
    - `CASE` statements for classifying revenue tiers (e.g., Low / Medium / High orders)
    - `DATEPART()` and `CONVERT()` functions to break dates into day, month, and weekday
    - **CTEs (Common Table Expressions)** to handle funnel stages and top-performers logic
    - **Window functions like `RANK()` and `ROW_NUMBER()`** to extract top 3 items by type
      
- **Pandas**:
  - Loaded and cleaned CSVs exported from SQL
  - Standardized column names and converted date fields
  - Performed grouping and aggregation (e.g., monthly revenue trend)

- **Plotly Express**:
  - Bar charts for top items and categories
  - Pie charts for time-of-day and order tier breakdowns
  - Line chart for revenue over time
  - Heatmap for time-of-day vs month revenue performance

- **Streamlit**:
  - KPIs using `st.metric()`
  - Interactive layout with `st.columns()` and `st.subheader()`
  - Easy deployment and caching with `@st.cache_data`

---

## 🧠 Key Insights by Visualization

### **📊 Monthly Revenue Trend**
- **Insight**: Revenue peaked between April and July 2022, with a sharp drop starting March 2023.
- **Actionable Takeaway**: Monitor what operational or seasonal factors contributed to the early 2022 success, and investigate the cause of 2023’s decline.

### **🏅 Top 10 Selling Items**
- **Insight**: Cold Coffee, Sugarcane Juice, and Panipuri are top sellers by volume.
- **Actionable Takeaway**: Consider upsell combos or promotions featuring these top items.

### **💰 Revenue by Item Type**
- **Insight**: Beverages outperform Fast Food in total revenue.
- **Actionable Takeaway**: Focus on expanding beverage offerings or bundling them with food for increased average order value.

### **⏰ Revenue by Time of Day**
- **Insight**: Sales are highest in the Afternoon and Night.
- **Actionable Takeaway**: Optimize staffing and inventory during these peak time slots.

### **🧾 Transaction Type Breakdown**
- **Insight**: Online and cash transactions are evenly split in revenue share.
- **Actionable Takeaway**: Maintain both payment infrastructures and analyze preferences by customer segment.

### **🏷️ Order Revenue Tier Distribution**
- **Insight**: 76.7% of orders fall into the High revenue tier.
- **Actionable Takeaway**: Introduce incentives to increase order value and shift more transactions into the Medium/High tiers.

### **⭐ Top 3 Items by Type**
- **Insight**: Beverages consistently dominate both volume and ranking across item types.
- **Actionable Takeaway**: Consider loyalty rewards or featured promotions based on beverage sales patterns.

### **📊 Revenue Heatmap: Time of Day vs. Month**
- **Insight**: Nights in Q2 and Q4 of 2022 showed consistently high revenue; early 2023 and beyond underperformed.
- **Actionable Takeaway**: Replicate successful marketing/timing strategies from 2022 to recover post-2023 declines.

---

## 📈 Project Workflow Overview

### 1. **Data Source & Collection**
- Dataset: [`Fast Food Sales Report`](https://www.kaggle.com/datasets/rajatsurana979/fast-food-sales-report)
- Raw data downloaded and imported into **SQL Server** for preprocessing.

### 2. **Data Cleaning & Modeling (SQL Server)**
- Created **8 SQL Views** for:
  - Aggregating revenue by item, category, transaction type, and time
  - Ranking top products using `ROW_NUMBER()` and `RANK()`
  - Categorizing revenue tiers using `CASE`
  - Parsing datetime into multiple dimensions (month, time of day)

### 3. **Data Export & Wrangling (Pandas)**
- Exported SQL views to `.csv`
- Cleaned column names and ensured datetime formats were standardized
- Grouped, sorted, and restructured data for visualization

### 4. **Data Visualization (Plotly Express)**
- Generated:
  - Bar charts (top items, item types)
  - Pie charts (time of day, transaction types, revenue tiers)
  - Line chart (monthly revenue)
  - Heatmap (revenue by month vs. time of day)

### 5. **App Development & Deployment (Streamlit)**
- Built dashboard using `st.metric()`, `st.columns()`, and `st.plotly_chart()`
- Deployed using **Streamlit Cloud**



