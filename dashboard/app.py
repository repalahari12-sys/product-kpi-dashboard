import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/sales_data.csv")

df["Revenue"] = df["Quantity"] * df["Price"]

st.title("📊 Product KPI Dashboard")

revenue = df["Revenue"].sum()
orders = len(df)
avg_order = revenue / orders

col1, col2, col3 = st.columns(3)

col1.metric("Revenue", f"₹{revenue:,.0f}")
col2.metric("Orders", orders)
col3.metric("Avg Order Value", f"₹{avg_order:,.0f}")

fig = px.bar(
    df,
    x="Product",
    y="Revenue",
    title="Revenue by Product"
)

st.plotly_chart(fig, use_container_width=True)