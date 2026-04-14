from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def forecast_sales(df):
    # Fit model
    model = ARIMA(df['sales'], order=(5,1,0))
    model_fit = model.fit()

    # Forecast next 30 days
    forecast = model_fit.forecast(steps=30)

    # Create future dates
    last_date = df['date'].iloc[-1]
    future_dates = pd.date_range(start=last_date, periods=31, freq='D')[1:]

    forecast_df = pd.DataFrame({
        'date': future_dates,
        'forecast': forecast
    })

    return forecast_df