.. dscore documentation master file, created by
   sphinx-quickstart on Thu Oct 14 15:13:32 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
dscore
======
*Dscore is a framework for evaluating models using orthogonal components*

Models are essential to science, and testing competing models for explaining the world is one of the most basic scientific activities.
Traditionally, the model that most closely reproduces reality is believed to be the most likely.
But models are increasingly multi-faceted, in that they are used for multiple purposes or they were created by coupling together multiple models.
How to balance competing interests within a single model is the main challenge that prompted us to create dscore,
which is a method of decomposing models in order to evaluate different aspects of their performance.
On one hand, this is useful for determing which aspects of a model may require revision,
but it also allows the modeler to separate out the best elements among several models and combine them as an ensemble,
analogous to how an audio engineer mixes together multiple tracks to form the best rendition of a musical piece.


For more information, refer to our article in JAMES (https:XXXXXXXXXXXX).

Quick start
-----------
Install the latest version of the code from github:

    $ python3 -m pip install -U git+git://github.com/USGS-python/dscore.git


```python
import dscore
```

Issue tracker
-------------
Please report any bugs, suggest enhancements, or ask questsions using the issue
tracker:

  https://github.com/USGS-python/dscore/issues


References
-----------------------
Geman, S., Bienenstock, E., & Doursat, R. (1992). Neural networksand the bias/variance dilemma. Neural Computation, 4 (1), 158.
doi:10.1162/neco.1992.4.1.1


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
