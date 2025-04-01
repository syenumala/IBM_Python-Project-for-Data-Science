import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_tesla_revenue(url):
    """Extracts Tesla revenue data from a webpage."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find_all("table", class_="historical_data_table")
        if not table:
            return pd.DataFrame()
        table = table[0]
        rows = table.find_all("tr")
        data = []
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            if cols:
                data.append(cols)
        df = pd.DataFrame(data, columns=["Date", "Revenue"])
        df = df[df['Revenue'].str.contains("$", na=False)]
        df['Revenue'] = df['Revenue'].str.replace(r'[$,]', '', regex=True)
        df['Date'] = pd.to_datetime(df['Date'])
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

# URL where Tesla revenue data is located
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Extract revenue data
tesla_revenue = get_tesla_revenue(url)

# Display the last five rows of the DataFrame
print(tesla_revenue.tail())