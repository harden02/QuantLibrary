import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math

def momentum_factor(equity_log_returns, formation_start, formation_end, use_gradient, r_squared):
    """
    Gradient of logarithmic returns analysis required to be selected as potential pick.
    use_gradient : Boolean
        Determines if momentum should be measured by a steady increase in log returns (gradient) or by the highest returns over the period
        NOTE: WHEN USE_GRADIENT MAKE SURE DATA IS NOT TOO GRANULAR OR WILL BE USELESS METHOD
    r_squared : float
        The threshold for the R-squared value to consider a stock as having good momentum.
    Returns
    -------
    List of indexes of original array representing equities that meet momentum requirements set.
    """
        
    momentum_returns = equity_log_returns.loc[formation_start:formation_end] #looks at raw log returns in year before holding period
    
    if not use_gradient:
        straight_returns = np.exp(momentum_returns.sum())
        top_percent = math.floor(0.2 * len(straight_returns))
        highest_momentum = straight_returns.nlargest(n=top_percent, keep='first')
        plt.style.use('seaborn')
        momentum_returns.plot(kind='line', figsize=(24, 15), title='log returns formation period', legend=None)
        return highest_momentum.index
        
    else:
        momentum_returns.drop(columns=momentum_returns.columns[momentum_returns.mean() < 0], inplace=True)
        momentum_returns.drop(columns=momentum_returns.columns[momentum_returns.iloc[-1] < 0], inplace=True)
        plt.style.use('seaborn')
        momentum_returns.plot(kind='line', figsize=(24, 15), title='log returns formation period', legend=None)
        regress_returns = momentum_returns.to_numpy()
        regress_returns = regress_returns.transpose()
        X = np.arange(len(regress_returns[0]))
        corr_coeff = np.empty((0, 2), float)
        for row in regress_returns:  #runs least squares regression on each row to work out movement of returns
            result = stats.linregress(x=X, y=row)
            corr_coeff = np.append(corr_coeff, [[result.slope, result.rvalue]], axis=0)
        #creates array with gradients in 1st column and corr coefficients in 2nd
        
        good_indexes = []
        for i in range(len(corr_coeff)):
            print(i)
            if (corr_coeff[i, 1])**2 > r_squared and corr_coeff[i, 0] > 0:  #CONDITION FOR STOCK PICKING
                good_indexes.append(i)
        momentum_returns = momentum_returns.iloc[:, good_indexes]
        return momentum_returns.columns #creates list of indexes with a correlation coefficient greater than r_squared choice to pick
    
def momentum_factor(equity_log_returns, formation_start, formation_end, use_gradient):
    """
    Parameters
    ----------
    equity_log_returns : Array
        Collection of equities to be analysed.
    formation_start : DATE
        Date slice of array to start initial formation period analysis.
    formation_end : DATE
        Date slice of array to provide endpoint of formation period analysis.
    use_gradient : Boolean
        Determines if momentum should be measured by a steady increase in log returns (gradient) or by the highest returns over the period
        NOTE: WHEN USE_GRADIENT MAKE SURE DATA IS NOT TOO GRANULAR OR WILL BE USELESS METHOD
    Returns
    -------
    Array of momentum based performance for the relevant indexes
    """
        
    momentum_returns = equity_log_returns.loc[formation_start:formation_end] #looks at raw log returns in time before holding period
    
    if not use_gradient:
        straight_returns = np.exp(momentum_returns.sum())
        plt.style.use('seaborn')
        momentum_returns.plot(kind='line', figsize=(24, 15), title='log returns formation period', legend=None)
        return straight_returns
        
    else:
        momentum_returns = momentum_returns.loc[(momentum_returns != 0).any(axis=1)]
        plt.style.use('seaborn')
        momentum_returns.plot(kind='line', figsize=(24, 15), title='log returns formation period', legend=None)
        regress_returns = momentum_returns.to_numpy()
        regress_returns = regress_returns.transpose()
        X = np.arange(len(regress_returns[0]))
        corr_coeff = np.empty((0, 2), float)
        for row in regress_returns:  #runs least squares regression on each row to work out movement of returns
            result = stats.linregress(x=X, y=row)
            corr_coeff = np.append(corr_coeff, [[result.slope, result.rvalue]], axis=0)
        #creates array with gradients in 1st column and corr coefficients in 2nd
        momentum_index = pd.DataFrame(corr_coeff, columns=['gradient', 'correlation_coeff'])
        momentum_index.index = momentum_returns.columns.values.tolist()
        return momentum_index
        
