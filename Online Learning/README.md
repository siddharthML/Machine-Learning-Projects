# Online Learning

Online learning is a method of machine learning where dynamic algorithms try to learn from data that becomes available sequentially. This is in contrast to the traditional offline approaches to statistical learning where models are trained on the entire data set at once or in batches.

This repository contains the code for the first part of my dissertation which aimed to advance the application of online learning techniques as a tool to predict commodity futures (aluminium and copper) prices, and compare their performance against offline time series models. The commodity data used has been from Shanghai Futures Exchange. 

In the Python Implementation folder I have recreated the online time series experiments conducted by Anava et al. in their paper *Online Learning for Time Series* (included here). Their experiments focused on 4 baseline models depending on the nature of changing coefficients with time, climate prediction and new york stock exchange data. I have  extended their experiments to include copper and aluminium futures prices.

# Supplementary Material

*Introduction to Online Convex Optimization* by Elad Hazan is essential reading to get into the details of how online time series models are optimized through various first and second order techniques like online convex optimization and online newton step. 
