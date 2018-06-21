# README

## What is this?

This is an attempt to build a model based on the datasets found on *The Winton Stock Market Challenge*, found on **Kaggle**.

## The file

My analysis and model are found in the file named *Stock Prediction*. 
This file is an *R Markdown* file, because it an elegant way of presenting R code.

## Datasets

The datasets used in this file are not uploaded to my *Github* repository as it is too large. 
The datasets may be obtained from Kaggle, at the competitions website.

The competition is called: *The Winton Stock Market Challenge*

The URL is: https://www.kaggle.com/c/the-winton-stock-market-challenge

## Status

For the competition, *Winton* provided us with a training dataset that contained 40,000 different stocks, 
each containing 25 unnamed features, and 5 days worth of stock returns.

Given a day *D*, the model to be build uses the previous two days and intraday minute-by-minute returns for that day up to minute 120, and the features.
The target variables are the remaining minute-by-minute returns from minute 121 to 180, as well as the return for the following two days.

The *"Stock Prediction.Rmd"* file contains descriptive analysis of the dataset, as well as a Random Forest model to predict day *D+1*.
*D+2* was not predicted as running the Random Forest model is time consuming, but the approach would be almost identical to predicting *D+1*.

An attempt to predict minute-by-minute returns has not been done yet. The way to do so would be to build an *ARIMA* model, as this is **Time Series** data.

The remainder of the project may not be completed, but that's not set in stone.