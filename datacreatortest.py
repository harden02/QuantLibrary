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

test = ds.readstockcsv("S&P500pricesadj.csv", "2020-01-01", "2023-01-01", "^GSPC", "1d", True)
momentumperiod = 10
holdperiod = 10
looptest = []
for i in range(0, 10):
    looptest.append(test[i])
looptest = np.asarray(looptest)