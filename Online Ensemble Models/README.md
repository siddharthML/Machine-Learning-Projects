# Online Ensemble Models / Online Learning from Experts

In machine learning ensemble methods use multiple learning algorithms to obtain better predictive performance than could be obtained from any of the constituent learning algorithms alone. In the online learning setting, data is fed into the ensemble one instance at a time. The ensemble, which consists of a finite set of alternative models, optimizes the result using some form of exponentially weighted averages or convex optimization.

For the second half of my dissertation which involved predicting aluminium and copper prices in the Shanghai Futures Exchange online ensemble models were the primary focus. This repository contains the R code used for setting up online ensemble models along with the dissertation write up.

Additional reading material on ensemble models and optimization is also provided in the form of book by Bianchi and Lugosi, *Prediction, Learning and Games*. 

The R package used for creating ensembles was Pierre Gaillard's **opera** package which can be found here: https://github.com/Dralliag/opera
