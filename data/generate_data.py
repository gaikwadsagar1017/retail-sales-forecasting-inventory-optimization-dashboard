import pandas as pd
import numpy as np

# Generate date range
dates = pd.date_range(start="2023-01-01", periods=365)

# Generate synthetic sales data
sales = 100 + np.random.normal(0, 10, 365)

# Create DataFrame
df = pd.DataFrame({
    "date": dates,
    "sales": sales
})

# Save to CSV
df.to_csv("data/raw/sales_data.csv", index=False)

print("Dataset generated successfully!")