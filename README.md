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

## Analytical Approach

Sales data is analyzed to identify patterns and trends across products, customers, locations, and time periods.

The analysis focuses on:
- Understanding historical performance and demand behavior
- Aggregating data at multiple levels to support planning and comparison
- Identifying trends that can inform future business decisions
- Preparing structured analytical outputs for reporting and downstream use

---

##  Tools & Technologies  
- **Excel** → Data cleaning & initial exploration  
- **SQL** → Data transformation, handling missing values, KPI calculation  
- **Power BI** → Dashboard design & DAX measures for advanced analytics  

---

##Dataset
The dataset contains retail sales transaction data with the following fields:

-InvoiceNo, StockCode, Description, Quantity  
-InvoiceDate, UnitPrice, Customer_Id, Country  

The data represents individual product-level transactions across customers and regions.

---

##  Reporting Outputs & Insights
 
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

## Reporting Outcomes

The reporting layer enables:
- Monitoring performance trends across time, products, and regions
- Comparing customer segments and order behavior
- Identifying consistently high-performing products and customers
- Supporting structured, data-driven decision-making

---

 ## Reporting Structure

The reporting structure is designed to be consistent and reusable:
- Standardized KPI definitions across visuals
- Consistent filters and slicers across pages
- Clear separation between data preparation and visualization logic
- Dashboard layout optimized for business stakeholder consumption




