import yfinance as yf
import pandas as pd

# Download Tesla stock data
tesla_data = yf.download("TSLA", period="max")

# Reset the index
tesla_data.reset_index(inplace=True)

# Save the DataFrame to a CSV file (optional)
# tesla_data.to_csv("tesla_stock_data.csv", index=False)

# Display the first five rows of the DataFrame
print(tesla_data.head())