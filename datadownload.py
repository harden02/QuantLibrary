import numpy as np
import pandas as pd
import datadownloader as dd
import datasetcreator as ds
import momentum_analysis as ma
import matplotlib.pyplot as plt
from scipy import stats
import math

dd.csv_creator("S&P500pricesadjfull.csv", "^GSPC", "2000-01-05", "2024-06-01", False)