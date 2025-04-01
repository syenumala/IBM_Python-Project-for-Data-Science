import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, title):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=('Historical Share Price', 'Historical Volume'), vertical_spacing=.3)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'].astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Bar(x=stock_data.index, y=stock_data['Volume'].astype("float"), name="Volume"), row=2, col=1)
    fig.update_layout(title_text=title, xaxis_rangeslider_visible=True)
    fig.show()

# Download Tesla stock data
tesla_data = yf.download("TSLA", period="max")

# Plot the graph
make_graph(tesla_data, "Tesla Stock Data")