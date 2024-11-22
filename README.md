# DS 5110: Final Project RetailDB
# Topic 
Managing a Retail Store Database and analysis (Big Data System)

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
- **Phase 4: Build visualizations and dashboards for insight and analysis.**
- **Phase 5: Optimizing and refining base one feedback.**

# Phase 1: Schema Design
![image](https://github.com/user-attachments/assets/5b78824e-0a02-49d9-ae34-5bb77afdd995)

## SQL cmd to create the database
CREATE TABLE Key_SKU(
        ProductSKU      TEXT PRIMARY KEY,
        stockCode       INTEGER
);
CREATE TABLE Online_Transactions(
        TransactionID INTEGER ,
        TransactionDate date,
        ProductSKU TEXT NOT NULL,
        ProductName TEXT,
        ProductCategory TEXT,
        Qty INTEGER,
        AvgPrice REAL,
        Revenue REAL,
        Tax REAL,
        Delivery REAL,
        PRIMARY KEY (TransactionID,TransactionDate,ProductSKU),
        FOREIGN KEY(ProductSKU) REFERENCES Key_SKU(ProductSKU)
);
CREATE TABLE Invoice(
        InvoiceNo INTEGER,
        InvoiceDate date,
        StockCode INTEGER,
        Qty Integer,
        PRIMARY KEY(InvoiceNo, InvoiceDate, StockCode),
        FOREIGN KEY(StockCode) REFERENCES Key_SKU(StockCode)
);
CREATE TABLE Market_Spending(
        SpendDate date PRIMARY KEY,
        offlineSpending REAL,
        onlineSpending REAL
);

# Phase 2：Retrieve and observe Raw Data and finalize DB structure.
Source data we used: https://www.kaggle.com/datasets/jpallard/google-store-ecommerce-data-fake-retail-data?select=Online.csv

# Phase 3: Import Data after cleaning and parsing.
First, we clean the normalized source data. 

With Colab using Python pandas, we merged entries with the same identifier to meet uniqueness for relational database importing. 

For example in retail source data, we have multiple entries with the same `InvoiceId` and `StockCode`.


