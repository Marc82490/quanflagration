import csv
import urllib.request
import numpy as np
import pandas as pd

def hist_stock_data(symbol, date):
    """Look up historical data for a symbol."""
    
    # reject symbol if it starts with caret
    if symbol.startswith("^"):
        return None

    # reject symbol if it contains comma
    if "," in symbol:
        return None
        
    # query Quandl
    # API key provided by Quandl
    API_KEY = 'cyMe7LzYpKy_5TX68KQN'

    url = "https://www.quandl.com/api/v3/datasets/WIKI/{}/data.csv?start_date={}&column_index=4&order=asc&api_key={}".format(symbol, date, API_KEY)
    webpage = urllib.request.urlopen(url)
    data = pd.read_csv(webpage)
    data.set_index("Date", inplace=True)