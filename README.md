D-score: the decomposed score method
=============================================
Models are essential to science, 
and testing competing models of explaining the world is one of the most basic scientific activities.
Traditionally, the model that most closely reproduces reality is believed to be the most likely.
But models are increasingly multi-faceted, in that they are used for multiple purposes or they were created by coupling together several models.
How to balance competing interests within a single model is the main challenge that prompted us to create D-score.
D-score is a method of decomposing models in order to understand different aspects of their performance.
Once decomposed, the best components can be selected among the models and recombined to form an optimal ensemble prediction.

What is D-score?
-----------------------
D-score is a framework for evaluating and scoring models by way of orthogonal decompositions;
a classic example being the decomposition of mean squared error (MSE) into bias and  variance (Geman et al., 1992).
Orthogonal decompositions are advantageous for two reasons.
First, they are easy to interpret. For example, when performing model inference with linear regression, we try to find orthogonal explantory variables;
otherwise it becomes difficult to discern how each variable affects the outcome:
some variables may act through other variables and as variables become correlated inferences become more unstable.
Similarly, when performing inference about other types of models
Second, when combined with other orthogonal decompositions, the resulting components are also orthogonal.
If each component represents a concept, then simple decompositions can be combined to represent more complex concepts,
just like words in a language.
In that sense, D-scores components form the basis of an expressive language through which to interrogate models and data.


Another main

A favorible p
Many . Often these 
D-score takes different approach. Instead of aggregagting

For more information, refer to our article in JAMES (https:XXXXXXXXXXXX).


If you discover mistakes in this library or want to suggest improvements, raise them as an [issue](https://github.com/USGS-python/dscore/issues).


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

