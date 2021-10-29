import matplotlib.pyplot as plt
import seaborn as sns

tick_label_size = 9


def ilamb_card(scores, vmin=0, vmax=100,
               component_labels=None,
               score_label=None,
               cmap='RdYlBu',
               reverse_cmap=False,
               hlines=None,
               cbar=False,
               annot_kws={"size": 8},
               ax=None):
    """

    Parameters
    ----------
    scores : pandas.DataFrame
        DataFrame with rows for each component
    vmin : float
    vmax : float
    score_labels : list
    hlines : list
           rows to place horizontal lines
    """
    if ax is None:
        fig, ax = plt.subplots(1)

    if component_labels is None:
        component_labels = scores.index

    # if score_label is None and hasattr(scores, 'name'):
    #    score_label = scores.name

    g = sns.heatmap(scores.round().astype(int),
                    vmin=vmin,
                    vmax=vmax,
                    yticklabels=component_labels,
                    annot=True,
                    fmt='d',
                    annot_kws=annot_kws,
                    cmap=cmap,
                    cbar=cbar,
                    square=True,
                    ax=ax)

    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=90)

    if hlines is not None:
        ax.hlines(hlines, *ax.get_xlim(), colors='k')

    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    ax.set_xlabel(score_label)
    ax.set_ylabel('Component')

    ax.tick_params(axis='y', labelsize=tick_label_size)
    ax.tick_params(axis='x', labelsize=tick_label_size)

    return g


def multi_panel_card(score_cards,
               score_labels,
               component_labels=None,
               hlines=None,
               figsize=None,
               tight_layout=True):
    """Helper function for plotting multiple score cards with the same components
    """

    fig, ax = plt.subplots(1, len(score_cards), figsize=figsize)
    fig.subplots_adjust(hspace=0)

    for i, score in enumerate(score_cards):
        ilamb_card(score,
                   score_label=score_labels[i],
                   hlines=hlines,
                   ax=ax[i])
        #import pdb; pdb.set_trace()
        if not ax[i].get_subplotspec().is_first_col():
            ax[i].set_yticklabels([])
            ax[i].tick_params(left=False)
            ax[i].set_ylabel('')
            
    fig.tight_layout()    
    return fig
