# Euroleague Prediction 🏀

# TLDR;            <img width="302" alt="Screen Shot 2021-04-12 at 2 50 25 PM" src="https://user-images.githubusercontent.com/66208179/114390089-7a10ee00-9b9e-11eb-84dd-930f2b829afd.png">

This repository includes an end-to-end analysis including machine learning algorithms to predict Euroleague Basketball results and rankings.

This is a binary classification problem, i.e. an observation must be classified as 1 (home win) or 2 (away win).

My implementation is based off of the paper [Descriptive and Predictive Analysis of Euroleague Basketball Games and the Wisdom of Basketball Crowds](https://paperswithcode.com/paper/descriptive-and-predictive-analysis-of). My main goal is to implement the ```future improvements``` section to improve accuracy.

### Challenges:
* Euroleague new format is only a few years old (after 2016).
* The number of games is much lower compared to NBA (less data).
* Euroleague teams change every season (not a closed championship like NBA).

### Notes:
* Involving injury stats has not affected the prediction results significantly.
* The glass ceiling: the maximum accuracy reached for NBA prediction was %74.


# Data Collection

I've used three separate datasets from Kaggle (see Code and Resources Used): 

- A dataset of team statistics.
- A dataset of player statistics.
- A dataset of game results and statistics.

# Exploratory Data Analysis

I first analyzed each dataset separately since their sources were different (see `players` and `euroleague` notebooks). In the main `analysis` notebook, I looked at the `games` dataset as the main data.

* Season 2016-2017 is referred as 2016.
* Added the target variable as 1 (home win) or 2 (away win).

Then, I merged all these dataframes to look at the information together and to model the data.

### Sneakpeek: Data Visualization Results

As the seasons progress, home teams tend to score more (the average home score has an increasing trend):

<img width="491" alt="Screen Shot 2021-04-11 at 5 58 29 PM" src="https://user-images.githubusercontent.com/66208179/114309358-8db14b80-9aef-11eb-9432-5c20174863ac.png">

I also figured that individual team stats would also be useful, so I added the `teams` data to the `analysis` notebook for team-level predictions.

<img width="393" alt="Screen Shot 2021-04-05 at 9 05 09 PM" src="https://user-images.githubusercontent.com/66208179/113612074-0760b980-9658-11eb-9c2c-3eb0d0028da9.png">

# Preparing the Data

(see `prepare_data.py` in `scripts` folder)

Includes:
- Scaling (Min Max Scaler)
- Feature Selection
- Categorical to Numerical Values

# Modeling

## Game Level Predictions

* Based on `games` data.

{'LogReg': 0.9958333333333333, 'KNN': 0.8791666666666667, 'RandomForest': 1.0}
 
 Test Accuracy with KNN:``` 0.82```

# Code and Resources Used

### Euroleague Data
```
- https://www.kaggle.com/vadimgladky/euroleague-basketball-results-20032019
- https://www.kaggle.com/avivshany/euroleague-basketball-advanced-stats
- https://www.kaggle.com/jacobbaruch/basketball-players-stats-per-season-49-leagues
```
