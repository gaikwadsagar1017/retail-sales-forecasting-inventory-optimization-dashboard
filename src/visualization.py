import matplotlib.pyplot as plt

def plot_forecast(df, forecast_df):
    plt.figure(figsize=(10,5))

    plt.plot(df['date'], df['sales'], label='Actual')
    plt.plot(forecast_df['date'], forecast_df['forecast'], label='Forecast')

    plt.legend()
    plt.title("Sales Forecast")
    plt.show()