# Guest Intelligence Dashboard 📊

An interactive analytics dashboard built with **Streamlit**, **Pandas**, and **Plotly** to visualize guest behavior and sales performance for a fast-food chain. This project aligns with the role of a **Guest Intelligence Analyst** by analyzing customer data, identifying trends, and presenting insights in a usable interface.

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


## 🌐 Live Demo
[Try the Dashboard on Streamlit Cloud](https://guestintelligenceanalysis-h6jjpeg6eyrn79zfbzuacu.streamlit.app/) 

---


