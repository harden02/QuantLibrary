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
    
    price_data = price_data.iloc[-period:]
    most_recent = price_data[-1]
    lowest = price_data.min()
    highest = price_data.max()
    
    oscillator = ((most_recent - lowest) / (highest - lowest)) * 100
    
    return oscillator
    
