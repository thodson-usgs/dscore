D-score
=======
*Dscore is a framework for evaluating models using orthogonal components*

Models are essential to science, and testing competing models for explaining the world is one of the most basic scientific activities.
Traditionally, the model that most closely reproduces reality is believed to be the most likely.
But models are increasingly multi-faceted, in that they are used for multiple purposes or they couple together multiple models.
How to balance such competing interests within a single model is the main challenge that prompted us to create D-score,
which is a framework for decomposing models to evaluate specific aspects of their performance.
On one hand, this is useful for determing which aspects of a model may require revision,
but it also allows the modeler to separate out the best elements among several models and combine them as an ensemble,
analogous to how an audio engineer mixes together multiple tracks to form the best rendition of a musical piece.

For more information, refer to our article in JAMES (https://doi.org/10.1029/2021MS002681) and the notebooks in this repo.

If use d-score in your work, please cite us our paper:

Hodson, T.O., Over, T.M., and Foks, S.F. (2021). Mean squared error, deconstructed.
Journal of Advances in Modeling Earth Systems.


Setup
-----
Install the latest version of the code from github:

    $ python3 -m pip install -U git+git://github.com/USGS-python/dscore.git
    
    
Issue tracker
-------------
Please report any bugs, suggest enhancements, or ask questsions using the issue
tracker:

  https://github.com/USGS-python/dscore/issues
