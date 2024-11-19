
DROP TABLE IF EXISTS Key_SKU;
CREATE TABLE Key_SKU(
	ProductSKU	TEXT PRIMARY KEY,
	stockCode	INTEGER
);

DROP TABLE IF EXISTS Online_Transactions;
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

DROP TABLE IF EXISTS Invoice;
CREATE TABLE Invoice(
	InvoiceNo INTEGER,
	InvoiceDate date,
	StockCode INTEGER,
	Qty Integer,
	PRIMARY KEY(InvoiceNo, InvoiceDate, StockCode),
	FOREIGN KEY(StockCode) REFERENCES Key_SKU(StockCode)
);

DROP TABLE IF EXISTS Market_Spending;
CREATE TABLE Market_Spending(
	SpendDate date PRIMARY KEY,
	offlineSpending REAL,
	onlineSpending REAL
);
