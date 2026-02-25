# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding = "latin1")

# Data cleaning
df.isnull().sum()
df.duplicated().sum()
df.describe()

df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df.isnull().sum()

# New columns for calculations
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month name"] = df["Order Date"].dt.strftime("%b")
df["Month-Year"] = df["Order Date"].dt.to_period("M").astype(str)
df["Profit margin"] = (df["Profit"] / df["Sales"]) * 100

df.to_csv('superstore_cleaned.csv', index = False)

# Calculate KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_val = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100
print("total sales:",total_sales)
print("total profit", total_profit)
print("total order", total_orders)
print("average order", avg_order_val)
print("profit marg:", profit_margin)

# Revenue trend over time
monthly_sales = df.groupby("Month-Year")["Sales"].sum().reset_index()
monthly_profit = df.groupby("Month-Year")["Profit"].sum().reset_index()

plt.figure(figsize=(10,4))
plt.plot(monthly_sales["Month-Year"], monthly_sales["Sales"], color="#1a80bb")
plt.gca().set_facecolor("#8cc5e3")
plt.gcf().set_facecolor("#8cc5e3")
plt.xticks(rotation=90)
plt.title("Monthly sales trends")
plt.xlabel("Month-Year")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(monthly_profit["Month-Year"], monthly_profit["Profit"], color="#1a80bb")
plt.xticks(rotation=90)
plt.gca().set_facecolor("#8cc5e3")
plt.gcf().set_facecolor("#8cc5e3")
plt.title("Monthly Profit trends")
plt.xlabel("Month-year")
plt.ylabel("Profit")
plt.show()

# Top selling products
top_sell_products = df.groupby("Product ID")["Sales"].sum().sort_values(ascending = False).head(10)

plt.figure(figsize=(10,4))
top_sell_products.plot(kind = "bar", color="#1a80bb")
plt.xticks(rotation=45)
plt.gca().set_facecolor("#8cc5e3")
plt.gcf().set_facecolor("#1a80bb")
plt.title("Top selling products")
plt.xlabel("Product ID")
plt.ylabel("Sales")
plt.show()

# High value categories and regions
cat_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
cat_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
reg_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
reg_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,4))
cat_sales.plot(kind = "bar", color="#1a80bb")
plt.xticks(rotation=45)
plt.gca().set_facecolor("#8cc5e3")
plt.gcf().set_facecolor("#1a80bb")
plt.title("High value categories sales")
plt.xlabel("Category")
plt.ylabel("sales")
plt.show()

plt.figure(figsize=(10,4))
cat_profit.plot(kind = "bar", color="#1a80bb")
plt.xticks(rotation=45)
plt.gca().set_facecolor("#8cc5e3")
plt.gcf().set_facecolor("#1a80bb")
plt.title("High value categories profit")
plt.xlabel("Category")
plt.ylabel("profit")
plt.show()

plt.figure(figsize=(10,4))
reg_profit.plot(kind = "bar", color="#1a80bb")
plt.xticks(rotation=45)
plt.gca().set_facecolor("#8cc5e3")
plt.gcf().set_facecolor("#1a80bb")
plt.title("High value regions")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()