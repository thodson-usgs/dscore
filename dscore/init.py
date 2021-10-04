import numpy as np
import pandas as pd

from statsmodels.tsa.seasonal import STL


## data frame versions
def tsv(e):
    """
    """
    res = STL(e, period=365, seasonal=9).fit()
    E = pd.DataFrame({'trend' : res.trend,
                      'seasonality' : res.seasonal,
                      'variability' : res.resid})
    return(E)
    
    
def bias_variance(e):
    """
    """
    bias = e.mean()**2
    bias.index = [i + '_bias' for i in bias.index]
    variance = e.var()
    variance.index = [i + '_var' for i in variance.index]

    return bias.append(variance)




def bds(x, x_h):
    """
    """
    e = x_h - x
    s = np.sort(x_h) - np.sort(x)
    var_s = s.var()
    var_e = e.var()
    
    e_bias = e.mean()**2
    e_dist = var_s
    e_seq = var_e - var_s
    names = ['bias','distribution','sequence']
    # compose
    return pd.Series([e_bias, e_dist, e_seq], index=names)


def bias_deviation(e):
    """
    """
    deviations = e - e.mean()
    bias = e - deviations
    
    return bias, deviations


def bds2(x, x_h):
    """
    Feed this deviations
    """
    e = x_h - x
    i_x = np.argsort(x)
    i_xh = np.argsort(x_h)
    #reverse_i = np.argsort(i_x)
    #s = x_h[i_xh].values - x[i_x].values
    s = np.sort(x_h) - np.sort(x)
    
    bias, deviation = bias_deviation(e)
    bias, distribution = bias_deviation(s)
    distribution = distribution[i_x]
    
    sequence = deviation - distribution
    sequence = deviation**2 - distribution**2
    #sequence = np.sqrt(np.abs(deviation**2 - distribution**2))
    
    return bias, distribution, sequence
 
def bds3(x, x_h):
    """
    Feed this deviations
    """
    e = x_h - x
    i_x = np.argsort(x)
    i_xh = np.argsort(x_h)
    #reverse_i = np.argsort(i_x)
    #s = x_h[i_xh].values - x[i_x].values
    s = np.sort(x_h) - np.sort(x)
    
    bias, distribution = bias_deviation(s)
    distribution = distribution[i_x]
    
    sequence = e - bias - distribution
    
    return bias, distribution, sequence
 
    
def bds4(x, x_h):
    """
    Feed this deviations
    """
    #import pdb; pdb.set_trace()
    e = x_h - x
    i_x = np.argsort(x)
    i_xh = np.argsort(x_h)
    #reverse_i = np.argsort(i_x)
    #s = x_h[i_xh].values - x[i_x].values
    #s = np.sort(x_h) - np.sort(x)
    #s = x -
    
    bias, deviation = bias_deviation(e)
    bias, distribution = bias_deviation(s)
    distribution = distribution[i_x]
    
    sequence = deviation - distribution
    
    return bias, distribution, sequence
    
    
def seasons(e):
    """
    """
    #import pdb; pdb.set_trace()
    names = ['winter','spring','summer','fall']
    winter = season(e, (e.index.month == 12) |  (e.index.month <= 2))
    spring = season(e, (e.index.month >2) & (e.index.month <= 5))
    summer = season(e, (e.index.month >5) & (e.index.month <= 8))
    fall = season(e, (e.index.month >8) & (e.index.month <= 11))
    
    return pd.Series([winter, spring, summer, fall], index=names)

def season(e, index):
    return ((e*index)**2).mean()
    
def distribution(x, x_h, 
                 quantiles=[0,0.25, 0.5, 0.75, 1],
                 labels=['low','below_avg','above_avg','high']):
    """
    quantiles = np.linspace(0,1,11)
    """
    s = np.sort(x_h) - np.sort(x)
    var_s = s.var()
    
    scores = []
    for i in range(len(quantiles) -1):
        x_hq = clip_quantile(x_h, quantiles[i], quantiles[i+1])
        x_q = clip_quantile(x, quantiles[i], quantiles[i+1])
        l = min(len(x_hq), len(x_q))
        s = np.sort(x_hq)[:l] - np.sort(x_q)[:l]
        scores.append(s.var())
        
    return pd.Series(scores, index=labels)
        

def clip_quantile(x, lower, upper):
    """
    Fix to include 1 in upper
    """
    u = x.quantile(upper)
    l = x.quantile(lower)
    index = (x>=l) & (x<u)
    return x[index]


def distribution(x, x_h, 
                 bins=4,
                 labels=['low','below_avg','above_avg','high']):
    """
    """
    s = np.sort(x_h) - np.sort(x)
    #var_s = s.var()
    stride = len(s)/bins 
    breaks = np.arange(0, len(s), stride)
    breaks = np.rint(breaks).astype(int).tolist()
    breaks.append(len(s))
    
    scores = []
    for i in range(len(breaks)-1):
        error_bin = s[breaks[i]: breaks[i+1]]
        #s = np.sort(x_hq)[:l] - np.sort(x_q)[:l]
        scores.append(error_bin.var())
        
    return pd.Series(scores, index=labels)


def quantiles(x, x_h, 
              quantiles=[0,0.25, 0.5, 0.75, 1],
              labels=['low','below_avg','above_avg','high']):
    """
    quantiles = np.linspace(0,1,11)
    """
    # sort for distribution decomp
    #s = np.sort(x_h) - np.sort(x)
    e = x_h - x
    scores = []
    ranks = x.rank(method='first')
    quants = pd.qcut(ranks, q = [0,0.25,0.5,0.75,1])
    for i in range(len(quantiles) -1):
        quant = e * (quants == quants.cat.categories[i]) # select quantile
        mse_q = ((quant)**2).mean()
        scores.append(mse_q)

    return pd.Series(scores, index=labels)
 

def mse(e):
    #e = x_h - x
    mse = (e**2).mean()
    
    return pd.Series([mse], index=['mse'])

def score(e, a=1):
    return np.exp(-1*a*e)
