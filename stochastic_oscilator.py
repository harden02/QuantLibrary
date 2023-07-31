# -*- coding: utf-8 -*-
"""
Implementation of Stochastic oscillator on dataset with custom period
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats

def calculate_oscillator(price_data, period):
    
    pricedata = price_data.iloc[-period:]
    most_recent = pricedata[-1]
    lowest = pricedata.min()
    highest = pricedata.max()
    
    oscillator = ((most_recent - lowest) / (highest - lowest)) * 100
    
    return oscillator
    
