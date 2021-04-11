# for games data

# fill missing values
def missing_values(games):
    """
    Takes the games dataframe and fills out the missing values.
    """
    games["FT%"].fillna(games["FT%"].mean(), inplace=True)
    
# feature selection
def feature_selection(games):
    """
    Takes the games dataframe and applies feature selection to the dataframe after.
    """
    
    # add the target feature
    games["wins"] = 0
    
    for k in range(len(games)):
        if games["win"][k] == True and games["location"][k] =="home_team":
            games["wins"][k] = 1
        if games["win"][k] == True and games["location"][k] =="away_team":
            games["wins"][k] = 2
    # drop unnecessary columns
    games.drop("game_id", axis = 1, inplace=True)
    games.drop("win", axis = 1, inplace = True)
    
def cat_to_num_games(games):
    """
    Takes the games dataframe and returns the dataframe with transformed categorical to numerical values.
    """
    cat_col = ["team", "location", "OP_team"]
    dummies = pd.get_dummies(games[cat_col])
    games = games.drop(cat_col, axis = 1)
    games = pd.concat([games, dummies], axis = 1)
    return games

# for games and teams

# scaling
def scaling(df):
    """
    Takes the games and teams dataframes separately and returns the dataframe after min-max scaling.
    """
    scaler = MinMaxScaler()
    transformed = scaler.fit_transform(df)
    # keep the column names
    cat_df = pd.DataFrame(transformed, columns = df.columns)
    df = cat_df
    return df
    
# for teams
def cat_to_num_teams(teams):
    """
    Takes the teams dataframe and returns the dataframe with transformed categorical to numerical values.
    """
    cat_col = ["team"]
    dummies = pd.get_dummies(teams[cat_col])
    teams = teams.drop(cat_col, axis = 1)
    teams = pd.concat([teams, dummies], axis = 1)
    return teams
    
def together(games, teams):
    """
    Returns the games and teams dataframes after all applications.
    """
    #games
    missing_values(games)
    feature_selection(games)
    games = cat_to_num_games(games)
    games = scaling(games)
    #teams
    teams = cat_to_num_teams(teams)
    teams = scaling(teams)
    return games, teams