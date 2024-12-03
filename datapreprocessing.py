# -*- coding: utf-8 -*-
"""DataPreprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f5qZgiSvT_lfLcpM6ziwjG-UyJ-Y5D_I
"""

#Cleaning up Missing, Duplicate, Negative, Outlier, Mistyped data

import pandas as pd

#Preprocessing KEY_SKU
keySKU = pd.read_csv('sourceData/KEY_SKU.csv')

#Check that all values are unique
keySKU.value_counts()

#Check for any missing values
keySKU[(keySKU['Product SKU'].isna()) | (keySKU['StockCode'].isna()) ]

keySKU.to_csv('cleanData/Clean_SKU.csv',index = False)

#Preprocessing Marketing_Spend
ms = pd.read_csv('sourceData/Marketing_Spend.csv')
ms.rename(columns={"Unnamed: 0":"Spend Date"})

#Replaces missing values with median values and drops duplicates
ms['Offline Spend'].fillna(ms['Offline Spend'].median(), inplace = True)
ms['Online Spend'].fillna(ms['Online Spend'].median(), inplace = True)
ms = ms.drop_duplicates()

ms.to_csv("cleanData/Clean_Marketing_Spend.csv", index = False)


online = pd.read_csv('sourceData/Online.csv')
online.head()
# Reformat the date in Online
online['Date'] = pd.to_numeric(online['Date'])
online['Date'] = pd.to_datetime(online['Date'], format='%Y%m%d')

for i in range(len(online.columns)):
  online[online.columns[i]].dropna()
online = online.drop_duplicates()

online = online.drop(online[online["Quantity"].isna()].index)

online.to_csv('cleanData/Clean_Online.csv', index = False)

retail = pd.read_csv('sourceData/Retail.csv')
for i in range(len(retail.columns)):
  retail[retail.columns[i]].dropna()
retail = retail.drop_duplicates()

retail.to_csv('cleanData/Clean_Retail.csv', index = False)