import numpy as np
import pandas as pd

from statsmodels.tsa.seasonal import STL


def stl(e):
    """Decompose error using STL.

    Seasonal and trend decomposition using Loess (STL).
    Note that STL is not perfectly orthogonal.

    Parameters
    ----------
    e : array_like


    References
    ----------
    .. [1] Cleveland et al., 1990, STL: A seasonal-trend decomposition
       procedure based on loess. Journal of Official Statistics, 6(1), 3-73.
    """
    res = STL(e, period=365, seasonal=9).fit()
    E = pd.DataFrame({'trend': res.trend,
                      'seasonality': res.seasonal,
                      'variability': res.resid})
    return(E)


def bias_variance(e):
    """Decompose error into bias and variance.

    Parameters
    ----------
    e : array_like

    Returns
    -------
    Series with entry for each component.

    References
    ----------
    .. [1] Geman et al., 1992, Neural networks and the bias/variance dilemma.
       Neural Computation, 4(1), 158. http://dx.doi.org/10.1162/neco.1992.4.1.1
    """
    bias = e.mean()**2
    bias.index = [i + '_bias' for i in bias.index]
    variance = e.var()
    variance.index = [i + '_var' for i in variance.index]

    return bias.append(variance)


def bias_distribution_sequence(x, x_h):
    """Bias-distribution-sequence decomposition

    Parameters
    ----------
    x : array_like
    x_h : array_like


    Returns
    -------
    Series with entry for each component.

    References
    ----------
    .. [1] Hodson et al., 2021 (accepted), Mean squared error, deconstructed.
    Journal of Advances in Earth Systems Modeling.
    """
    e = x_h - x
    s = np.sort(x_h) - np.sort(x)
    var_s = s.var()
    var_e = e.var()

    e_bias = e.mean()**2
    e_dist = var_s
    e_seq = var_e - var_s
    names = ['bias', 'distribution', 'sequence']
    return pd.Series([e_bias, e_dist, e_seq], index=names)


def bias_deviation(e):
    """
    TODO data decomposition
    """
    deviations = e - e.mean()
    bias = e - deviations

    return bias, deviations


def seasons(e):
    """Decompose error by season.

    Parameters
    ----------
    e : DataFrame

    """
    def season(e, index):
        return ((e*index)**2).mean()

    names = ['winter', 'spring', 'summer', 'fall']
    winter = season(e, (e.index.month == 12) | (e.index.month <= 2))
    spring = season(e, (e.index.month > 2) & (e.index.month <= 5))
    summer = season(e, (e.index.month > 5) & (e.index.month <= 8))
    fall = season(e, (e.index.month > 8) & (e.index.month <= 11))

    return pd.Series([winter, spring, summer, fall], index=names)


def by_index(e, index):
    """Decompose error by an index.

    TODO

    Parameters
    ----------
    e : array_like
    index : array_like
    """
    pass


def quantiles(x, x_h,
              quantiles=[0, 0.25, 0.5, 0.75, 1],
              labels=['low', 'below_avg', 'above_avg', 'high']):
    """
    quantiles = np.linspace(0,1,11)
    """
    e = x_h - x
    scores = []
    ranks = x.rank(method='first')
    quants = pd.qcut(ranks, q=[0, 0.25, 0.5, 0.75, 1])
    for i in range(len(quantiles) - 1):
        quant = e * (quants == quants.cat.categories[i])  # select quantile
        mse_q = ((quant)**2).mean()
        scores.append(mse_q)

    return pd.Series(scores, index=labels)


def mse(e):
    """ Mean squared error.
    """
    mse = (e**2).mean()

    return pd.Series([mse], index=['mse'])


def score(e, a=1):
    """Scores and error.

    Exponential scoring function that maps MSE to the unit interval.

    Parameters
    ----------
    e : array_like

    a : float
        Positive tuning parameter.

    References
    ----------
    .. [1] Collier et al., 2018, The International Land Model Benchmarking
    (ILAMB) system: Design, theory, and implementation. Journal of Advances
    in Modeling Earth Systems, 10(11), http://dx.doi.org/10.1029/2018ms001354
    """
    return np.exp(-1*a*e)
