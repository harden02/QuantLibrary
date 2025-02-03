# -*- coding: utf-8 -*-
"""
Downloader to retrieve csv of EOD adj close stock data from given list of symbols (i.e downloaded list of S&P500 symbols)
"""
import pandas as pd
import yfinance as yf

def csv_creator(output_loc, baseline, start_date, end_date, include_spy):
    """
    Parameters
    ----------
    file_loc : String
        location of csv/spreadsheet containing stock names for download
    baseline : String
        Name of Baseline reference for performance comparison (e.g S&P500 overall)
    start_date: String
        Start date
    end_date: String
        End date
    include_spy: Boolean
        include download of S&P500 SPY ETF for performance reference

    Returns
    -------
    csvs with relevant price data

    """

    file_loc = 'C:/Users/jakey/Documents/Python Finance/ETF Data/constituents_csv.csv'
    df = pd.read_csv(file_loc)
    df.dropna(inplace=True)
    stocks = df.iloc[:, 0].tolist()
    stocks.append(baseline)
    data = yf.download(stocks, start=start_date, end=end_date, interval='1d') 
    price_data = data.drop(["Close", "High", "Low", "Open", "Volume"], axis=1)
    price_data.columns = price_data.columns.droplevel(level=0) 
    price_data.to_csv(output_loc)
    
    if include_spy:
        spy_data = yf.download('SPY', start=start_date, end=end_date, interval='1d') 
        spy = spy_data.drop(["Close", "High", "Low", "Open", "Volume"], axis=1)
        spy.to_csv('SPYpricesadj.csv')
    
    return