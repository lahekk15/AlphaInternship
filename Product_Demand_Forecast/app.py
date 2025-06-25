import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error

st.title("Product Demand Forecasting")

# 1. Upload Dataset
uploaded_file = st.file_uploader("Upload your sales dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # 2. Basic Checks
    if 'date' not in df.columns or 'product' not in df.columns or 'sales' not in df.columns:
        st.error("Dataset must contain 'date', 'product', and 'sales' columns.")
    else:
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        # 3. Product Selection
        products = df['product'].unique()
        selected_product = st.selectbox("Select a Product to Forecast", products)

        product_df = df[df['product'] == selected_product].copy()
        product_df.set_index('date', inplace=True)
        
        st.line_chart(product_df['sales'], use_container_width=True)

        # 4. Forecast Settings
        forecast_period = st.slider("Forecast Period (Days)", min_value=7, max_value=90, value=30)

        if st.button("Generate Forecast"):
            try:
                model = ExponentialSmoothing(product_df['sales'], trend='add', seasonal='add', seasonal_periods=12).fit()
                forecast = model.forecast(steps=forecast_period)
                
                # Plot
                fig, ax = plt.subplots(figsize=(10, 4))
                product_df['sales'].plot(ax=ax, label='Historical Sales')
                forecast.plot(ax=ax, label='Forecast', color='orange')
                plt.title(f"Forecast for {selected_product}")
                plt.legend()
                st.pyplot(fig)
                
            except Exception as e:
                st.error(f"Error: {e}")
