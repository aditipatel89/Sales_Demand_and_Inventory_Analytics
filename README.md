#  Sales_Demand_and_Inventory_Analytics Project  

This project showcases an **end-to-end ETL pipeline and interactive Power BI dashboard** for analyzing customer and product sales patterns.  

---

## Business Context

This project simulates a demand, sales, and inventory planning scenario similar to enterprise supply chain and manufacturing environments.

The objective of the project is to:
- Analyze historical sales data to support demand forecasting
- Monitor product performance and availability indicators
- Support planning and purchasing decisions
- Provide standardized analytical reporting for business stakeholders

---

##  Tools & Technologies  
- **Excel** → Data cleaning & initial exploration  
- **SQL** → Data transformation, handling missing values, KPI calculation  
- **Power BI** → Dashboard design & DAX measures for advanced analytics  

---

##  Dataset  
The dataset contains retail sales transactions with the following fields:  
- `Item Identifier`, `Item Type`, `Item Weight`, `Item Visibility`  
- `Outlet Identifier`, `Outlet Type`, `Outlet Size`, `Outlet Location Type`  
- `Sales`, `Rating`, `Customer_ID`, `Country`  

---

##  Key Insights from the Dashboard  
1. **KPIs**:  
   - **Total Quantity Sold**: 541.91K  
   - **Average Order Value**: 376.38 USD  

2. **Customer Analysis**:  
   - Known vs Unknown Customers (segmentation)  
   - Order Size split into Above/Below Average  

3. **Revenue Insights**:  
   - Trend over **Year, Quarter, and Month**  
   - Revenue distribution by **Country**  
   - Revenue by **Product Description**  
   - Top Customers contributing to revenue  

4. **Interactive Filters**:  
   - **Month selection**  
   - **Unit Price range slicer**  

---

##  Dashboard Preview  
![image alt](https://github.com/aditipatel89/Sales_Analytics/blob/181dfeec7be989d70f73ebfc6305884c4e99ed6e/SalesData_screenshot.png)

---

##  Outcome  
The dashboard enables:  
- Identifying **sales trends** across time and countries  
- Segmenting **customers by size & order value**  
- Pinpointing **top-performing products & customers**  
- Supporting **data-driven decision-making** for sales optimization  

---

##  How to Use  
1. Clone this repository  
2. Load `cleaned_sales_data.xlsx` into Power BI  
3. Open `Sales_Dashboard.pbix` to explore the dashboard  

---


