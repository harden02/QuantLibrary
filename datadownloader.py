# -*- coding: utf-8 -*-
"""
Downloader to retrieve csv of EOD adj close stockdata from given list of symbols (i.e downloaded list of S&P500 symbols)
"""
import pandas as pd
import yfinance as yf

def csv_creator(output_loc, baseline, startdate, enddate, includeSPY):
    
    """
    Parameters
    ----------
    file_loc : String
        location of csv/spreadsheet containing stock names for download
    baseline : String
        Name of Baseline refernece for performance comparison (e.g S&P500 overall)
    startdate: String
        Start date
    enddate: String
        End date
    includeSPY: Boolean
        include download of S&P500 SPY ETF for performance reference

    Returns
    -------
    csvs with relevant pricedata

    """

    file_loc='C:/Users/jakey/Documents/Python Finance/ETF Data/constituents_csv.csv'
    df=pd.read_csv(file_loc)
    df.dropna(inplace=True)
    stocks=df.iloc[:,0].tolist()
    stocks.append(baseline)
    data=yf.download(stocks, start=startdate, end=enddate, interval='1d') 
    pricedata=data.drop(["Close", "High", "Low", "Open", "Volume"], axis=1)
    pricedata.columns=pricedata.columns.droplevel(level=0) 
    pricedata.to_csv(output_loc)
    
    if includeSPY:
        SPYd=yf.download('SPY', start=startdate, end=enddate, interval='1d') 
        SPY=SPYd.drop(["Close", "High", "Low", "Open", "Volume"], axis=1)
        SPY.to_csv('SPYpricesadj.csv')
    
    return