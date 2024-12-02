# DS 5110: Final Project RetailDB

# Topic 
**Managing a Retail Store Database and analysis (Big Data System)**

# Teams and Roles
- **Cheng Shi**: Database Schema Design and Importing
- **Daniel Xiong**: Data Parsing and Cleaning
- **Manish Kanuri**: Data Analysis and visualization

# Project Scope
This project is about designing a database system for managing a retail store, including product inventory,
sales transactions, and customer data. Then, Retrieve raw data from multiple resources and import it into the database after
cleaning and parsing. In the end, Build visualizations and dashboards for insight and analysis. such as Sales
Performance Evaluation and Employee Performance or Inventory Management Dashboard

# Development Plan
- **Phase 1: Design DB initial Schema** 
- **Phase 2: Retrieve and observe Raw Data and finalize DB structure.**
- **Phase 3: Import Data after cleaning and parsing.**
- **Phase 4: Analysis and visualization for insight.**
- **Phase 5: Build website to showcase.**

# Phase 1: Schema Design
### ER Diagram
![image](https://github.com/user-attachments/assets/5b78824e-0a02-49d9-ae34-5bb77afdd995)

### Create Database
The SQL command to create the tables located at: `SQLCode\CreateCSV.sql`  
Cmd to run: `python SQLCode\CreateCSV.sql`

# Phase 2：Retrieve and observe Raw Data and finalize DB structure.
### Source data
After reasearching and browsing, we decided to use this dataset from kaggle which is a sales data of a ecommerce website.  
（https://www.kaggle.com/datasets/jpallard/google-store-ecommerce-data-fake-retail-data?select=Online.csv）

# Phase 3: Import Data after cleaning and parsing.
First, we clean the normalized source data. 

With Colab using Python pandas, we merged entries with the same identifier to meet uniqueness for relational database importing. 

For example in retail source data, we have multiple entries with the same `InvoiceId` and `StockCode`.

Then we import the data into database using SQL script located: `SQLCode\ReadCSV.sql`.

# Phase4 : Analysis and visualization for insight.
After we import out sqlite database into colab notebook. We had a brainstrom about potential analysis idea will generate insight that can help the bussniess.
And here is the finalized topic we analysed:

1. **Item poplarity (Order item base on Amount of transaction)**
2. **Revenue Analysis (Top Categories/Products by Revenue)**
3. **Sales Trends Over Time (Total sales of each Month this Year)**
4. **Tax and Delivery Cost Impact**
5. **Profitability Analysis**
6. **High-Tax Impact Products**
7. **Revenue by Day of the Week**
8. **Item Popularity**

# Phase5 : Analysis and visualization for insight.
We utilized the visualization tools and library from python to genrate stright foward digram and have a website hosting the results.
![image](https://github.com/user-attachments/assets/188d9738-5940-4bac-a498-0d0e57be32f6)






