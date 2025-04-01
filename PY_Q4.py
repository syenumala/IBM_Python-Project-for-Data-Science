import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_gme_revenue(url):
    """Extracts GameStop revenue data from a webpage."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find_all("table", class_="historical_data_table")
        if not table:
            return pd.DataFrame() # Return empty DataFrame if no table found
        table = table[0] # Select the first table, as it's typically the revenue table.
        rows = table.find_all("tr")
        data = []
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            if cols:
                data.append(cols)
        df = pd.DataFrame(data, columns=["Date", "Revenue"])
        df = df[df['Revenue'].str.contains("$", na=False)] #filter out bad rows
        df['Revenue'] = df['Revenue'].str.replace(r'[$,]', '', regex=True) #remove $ and commas
        df['Date'] = pd.to_datetime(df['Date']) #convert date column to datetime object.
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

# URL where GameStop revenue data is located
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Extract revenue data
gme_revenue = get_gme_revenue(url)

# Display the last five rows of the DataFrame
print(gme_revenue.tail())