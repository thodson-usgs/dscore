import matplotlib.pyplot as plt
import seaborn as sns

tick_label_size = 9


def ilamb_card(scores, vmin=0, vmax=100,
               component_labels=None,
               score_label=None,
               hlines=None,
               ax=None):
    """

    Parameters
    ----------
    scores : pandas.Series
    vmin : float
    vmax : float
    score_labels : list
    hlines : list
           rows to place horizontal lines
    """
    if ax is None:
        pass

    if component_labels is None:
        component_labels = scores.index

    if score_label is None:
        score_label = scores.name

    sns.heatmap(scores.round().astype(int),
                vmin=vmin,
                vmax=vmax,
                yticklabels=component_labels,
                annot=True,
                fmt='d',
                annot_kws={"size": 8},
                cmap='RdYlBu',
                square=True,
                ax=ax)

    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=90)

    ax.hlines(hlines, *ax.get_xlim(), colors='k')

    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    ax.set_xlabel(score_label)
    ax.set_ylabel('Component')

    ax.tick_params(axis='y', labelsize=tick_label_size)
    ax.tick_params(axis='x', labelsize=tick_label_size)


def multi_card(*scores,
               component_labels=None
               score_labels=None,
               hlines=None,
               figsize=None):
    """Helper function
    """

    fig, ax = plt.subplots
    fig.subplots_adjust(hspace=0)

    for i, score in enumerate(scores):
        ilamb_card(score,
                   # score_label=score_labels[i],
                   hlines=hlines,
                   ax=ax[i])
