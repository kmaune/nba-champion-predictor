# nba-champion-predictor

The  overall goal of this project is to use machine learning methods to train a learner that will predict the most likely NBA champions next season. 

The learner will give each team a score for the season with values closer to 1 meaning more likely to be nba champion. As a reference point, here are [FiveThirtyEight's projections](https://projects.fivethirtyeight.com/2020-nba-predictions/) for next season. 

If you are having trouble viewing the Jupyter Notebook on Github, it can be [viewed here](https://nbviewer.jupyter.org/github/kmaune/nba-champion-predictor/blob/master/nba%20analysis.ipynb) as well

##Project Breakdown

This project can be broken down into 4 main parts:

1. Data analysis, feature selection and transformation on dataset of team statistics/results from previous seasons. 
2. Train a learner on the dataset of past season results
3. Projection of 2020 stats for individual players and teams based on past season stats
4. Use these projections as input to the trained learner and get predictions for next season