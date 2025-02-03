"""
Testing for the dataset creator
"""
import numpy as np
import pandas as pd
import data_downloader as dd
import dataset_creator as ds
import momentum_analysis as ma
import matplotlib.pyplot as plt
from scipy import stats
import math

test_data = ds.read_stock_csv("S&P500pricesadj.csv", "2020-01-01", "2023-01-01", "^GSPC", "1d", True)
momentum_period = 10
hold_period = 10
loop_test = []
for i in range(0, 10):
    loop_test.append(test_data[i])
loop_test = np.asarray(loop_test)