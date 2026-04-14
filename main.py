from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.forecasting import forecast_sales
from src.inventory import calculate_inventory
from src.visualization import plot_forecast

# Load data
df = load_data("data/raw/sales_data.csv")

# Preprocess
df = preprocess_data(df)

# Forecast
forecast_df = forecast_sales(df)

# Inventory optimization
inventory_df = calculate_inventory(df, forecast_df)

# Visualization
plot_forecast(df, forecast_df)

print(inventory_df.head())