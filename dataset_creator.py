"""Modularised data processor for S&P500 csv data (will extend to any stockprice csv eventually)"""
import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar

#Takes in local S&P500 csv in this folder and processes it for stock close prices over a certain time period and interval
#Generates logarithmic returns file and log returns in relation to the ETF that is being tracked


def read_stock_csv(file, start_date, end_date, etf_name, interval, blind):
    """
    

    Parameters
    ----------
    file : path
        csv of stock prices to be read.
    start_date : DATE
        start date for analysis.
    end_date : DATE
        end date for analysis.
    etf_name : STRING
        ticker symbol for ETF present in the stock file that it's following.
    interval : STRING
        interval to sample, i.e 3BMS for 3 business months or B for each business day.
    blind : BOOLEAN
        if true, removes indexes and dates from dataset, good for blind statistical research

    Returns
    -------
    final_prices : ARRAY
        Resampled and corrected stock prices.

    """
    
    price_data_raw = pd.read_csv(file, parse_dates=True, infer_datetime_format=True, index_col="Date")
    price_data_raw.sort_index(inplace=True)
    price_data = price_data_raw[start_date:end_date] #must be a quicker way of doing this without first reading in csv, look up for future
    if blind:
        price_data.drop(etf_name, axis=1, inplace=True)
        price_data.dropna(axis=1, inplace=True)
        final_prices_array = price_data.to_numpy()
        return final_prices_array
    else:
        price_data_resample = price_data.resample(interval).asfreq()
        final_prices = pd.merge_asof(price_data_resample, price_data, on="Date", allow_exact_matches=True, direction="backward")
        final_prices.dropna(axis=1, inplace=True)
        final_prices.columns = final_prices.columns.str.strip('_y')
        final_prices.set_index("Date", inplace=True)
        return final_prices


def logreturn(stockdata, ETFname, relativereturn):
    """
    

    Parameters
    ----------
    stockdata : ARRAY
        stock price array to calculate log returns on.
    ETFname : SRRING
        ETF name.
    relativereturn : BOOLEAN
        If yes, will return equivalent dataframe with relative returns to baseline ETF

    Returns
    -------
    dict
        returns a dictionary containing two arrays, absolute log returns and log returns relative to ETF.

    """
    logreturns=np.log(stockdata/stockdata.shift(1))  #calculates log returns for each
    if relativereturn == True:
        relativelogreturns=pd.DataFrame()  #have to create new dataframe otherwise following part doesn't work
        for column in logreturns:  
            relativelogreturns[column]=logreturns[column]-logreturns[ETFname]  #compares log returns to those of ETF
        return {"logreturns" : logreturns, "relativelogreturns" :relativelogreturns}
    else:
        return logreturns
