import numpy as np
import pandas as pd

def calculate_inventory(df, forecast_df):
    lead_time = 7
    service_level = 1.65  # 95%

    # Use historical sales for variability
    demand_std = np.std(df['sales'])

    # Use forecast for future demand
    avg_demand = np.mean(forecast_df['forecast'])

    # Safety stock formula
    safety_stock = service_level * demand_std * np.sqrt(lead_time)

    # Reorder point formula
    reorder_point = avg_demand * lead_time + safety_stock

    # Create output table
    result = pd.DataFrame({
        "Metric": ["Avg Demand", "Safety Stock", "Reorder Point"],
        "Value": [avg_demand, safety_stock, reorder_point]
    })

    return result