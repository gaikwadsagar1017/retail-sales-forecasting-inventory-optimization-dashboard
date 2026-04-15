import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.forecasting import forecast_sales
from src.inventory import calculate_inventory

# Page config
st.set_page_config(page_title="Retail Forecast Dashboard", layout="wide")

st.title("🛒 Retail Sales Forecasting & Inventory Optimization")

# Sidebar
st.sidebar.header("Settings")

data_path = st.sidebar.text_input("Dataset Path", "data/raw/sales_data.csv")

if st.sidebar.button("Run Analysis"):

    # Load data
    df = load_data(data_path)
    df = preprocess_data(df)

    st.subheader("📊 Raw Data")
    st.dataframe(df.head())

    # Plot Sales Trend
    st.subheader("📈 Sales Trend")

    fig1, ax1 = plt.subplots()
    ax1.plot(df['date'], df['sales'])
    ax1.set_title("Sales Over Time")
    st.pyplot(fig1)

    # Forecast
    forecast_df = forecast_sales(df)

    # Plot Forecast
    st.subheader("📉 Forecast vs Actual")

    fig2, ax2 = plt.subplots()
    ax2.plot(df['date'], df['sales'], label='Actual')
    ax2.plot(forecast_df['date'], forecast_df['forecast'], label='Forecast')
    ax2.legend()
    st.pyplot(fig2)

    # Inventory Calculation
    inventory_df = calculate_inventory(df, forecast_df)

    st.subheader("📦 Inventory Optimization")

    st.table(inventory_df)

    # Reorder Alert
    reorder_point = inventory_df[inventory_df['Metric'] == 'Reorder Point']['Value'].values[0]
    avg_demand = inventory_df[inventory_df['Metric'] == 'Avg Demand']['Value'].values[0]

    if avg_demand > reorder_point:
        st.error("⚠️ Reorder Needed!")
    else:
        st.success("✅ Stock Level Safe")

else:
    st.info("👈 Click 'Run Analysis' to start")