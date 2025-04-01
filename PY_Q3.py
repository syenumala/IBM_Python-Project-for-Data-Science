import yfinance as yf
import pandas as pd

# Download GameStop stock data
gme_data = yf.download("GME", period="max")

# Reset the index
gme_data.reset_index(inplace=True)

# Save the DataFrame to a CSV file (optional)
# gme_data.to_csv("gme_stock_data.csv", index=False)

# Display the first five rows of the DataFrame
print(gme_data.head())