# Machine-Learning with R

Unlike Python, R does not have a standardized interface for all its ML algorithms. Hence, for any non-trivial experiments, unifying the output of different algorithms becomes a tedious task. Additionally it requires us to implement infrastructure to resample models, optimize hyperparameters, select features, cope with pre- and post-processing of data and compare models in a statistically meaningful way. As this becomes computationally expensive, a need arises to parallelize these experiments as well. 

The **mlr** package is a machine-learning wrapper that covers most of these aspects and provides framework for classification, regression and survival analysis tasks along with  their corresponding evaluation and optimization methods, as well as unsupervised methods like clustering. It also has great flexibility in its implementation allowing introduction of new algorithms not on the standard list into the wrapper.

More details can be read on their official website: https://mlr.mlr-org.com/

This repository contains two folders. The first is MLT toolbox library which contains some practice code on how to implement different aspects of the MLR wrapper. The second is an assignment for STATG019 which required predicting wine quality using ML algorithms which extensively used this wrapper and systematically went through all aspects of an ML experiment: from pre-processing to model validation.
