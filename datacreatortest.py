"""
Testing for the dataset creator
"""
import numpy as np
import pandas as pd
import datadownloader as dd
import datasetcreator as ds

test = ds.readstockcsv("S&P500pricesadj.csv", "2010-02-01", "2023-01-01", "^GSPC", "1d")

