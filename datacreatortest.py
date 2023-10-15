"""
Testing for the dataset creator
"""
import numpy as np
import pandas as pd
import datadownloader as dd
import datasetcreator as ds
import momentum_analysis as ma
import matplotlib.pyplot as plt
from scipy import stats
import math

test = ds.readstockcsv("S&P500pricesadj.csv", "2010-02-01", "2023-01-01", "^GSPC", "1d")
stockdata = ds.logreturn(test, "^GSPC")
stuff = stockdata["logreturns"]
momentumreturns=stuff.loc["2022-01-10" : "2022-09-10"] #looks at raw log returns in time before holding period
straightreturns = np.exp(momentumreturns.sum())
plt.style.use('seaborn')
momentumreturns.plot(kind='line', figsize=(24, 15), title='log returns formation period', legend=None)
positivemomentum= straightreturns[straightreturns>1]
successfulstocks = momentumreturns.loc["2022-01-10" : "2022-09-10", positivemomentum.index.values.tolist()]
successfulstocks.plot(kind='line', figsize=(24,15), title='positive momentum picks', legend=True)
#momentumindications = ma.momentumfactor(stuff, "2022-01-10", "2022-09-10", False)



