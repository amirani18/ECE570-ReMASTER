import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# import mplfinance as mpf
import pandas as pd

# Load the data to examine its structure
file_path = '/Users/areejmirani/Desktop/ReMASTER/data/NQ_5Years_8_11_2024.csv'
data = pd.read_csv(file_path)

# Display the first few rows and summary information to understand the data structure
data.head(), data.info()


# Convert the 'Time' column to datetime for easier handling in plotting
data['Time'] = pd.to_datetime(data['Time'], format='%m/%d/%Y %H:%M')
data.set_index('Time', inplace=True)

# Resample the data to daily to simplify the visualization
daily_data = data.resample('D').agg({
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last',
    'Volume': 'sum'
})

# Plot 1: Time Series Line Chart for Close Price
plt.figure(figsize=(14, 6))
plt.plot(daily_data.index, daily_data['Close'], label='Close Price', color='blue')
plt.title('Daily Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: Volume Over Time
plt.figure(figsize=(14, 6))
plt.bar(daily_data.index, daily_data['Volume'], color='orange', width=1)
plt.title('Daily Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()

# Plot 3: Candlestick Chart for Price (OHLC)
mpf.plot(daily_data, type='candle', style='charles', volume=True, title='Daily Candlestick Chart with Volume')
