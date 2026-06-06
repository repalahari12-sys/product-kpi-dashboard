import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("data/sales_data.csv")

# Create Revenue Column
df["Revenue"] = df["Quantity"] * df["Price"]

# Dashboard Title
st.title("📊 Product KPI Dashboard")

# KPIs
total_revenue = df["Revenue"].sum()
total_orders = len(df)
avg_order_value = total_revenue / total_orders

col1, col2, col3 = st.columns(3)

col1.metric("Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Orders", total_orders)
col3.metric("Avg Order Value", f"₹{avg_order_value:,.0f}")

# Revenue by Product
fig = px.bar(
    df,
    x="Product",
    y="Revenue",
    title="Revenue by Product"
)

st.plotly_chart(fig, use_container_width=True)

# Category Analysis
category_sales = df.groupby("Category")["Revenue"].sum().reset_index()

fig2 = px.pie(
    category_sales,
    names="Category",
    values="Revenue",
    title="Category Wise Revenue"
)

st.plotly_chart(fig2, use_container_width=True)