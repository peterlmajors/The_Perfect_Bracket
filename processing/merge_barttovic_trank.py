# Import Packages
import pandas as pd

def merge_barttovic_trank(mdcm: pd.DataFrame, years: list[int]):
    
    # Create Team Season ID Column
    mdcm['team1_team_season'] = mdcm['team1_teamname'] + "_" + mdcm['season'].astype(str)
    mdcm['team2_team_season'] = mdcm['team2_teamname'] + "_" + mdcm['season'].astype(str)
    
    df_list = []
    for year in years:
        df = pd.DataFrame()
        
        # Merge Team 1 Stats
        barttovic = pd.read_csv(f'data/barttovic/trank/barttovic_trank_{year}.csv').drop(columns='Unnamed: 0').add_prefix('team1_') 
        df = pd.merge(left = mdcm[mdcm['season'] == year], right = barttovic, on = 'team1_team_season', how = 'left')
        
        # Merge Team 2 Stats
        barttovic = pd.read_csv(f'data/barttovic/trank/barttovic_trank_{year}.csv').drop(columns='Unnamed: 0').add_prefix('team2_')       
        df = pd.merge(left = df[df['season'] == year], right = barttovic, on = 'team2_team_season', how = 'left')
        
        df_list.append(df)
        
    # Concat DFs, Lowercase Column Names, and Export
    df = pd.concat(df_list, ignore_index=True)
    df.columns = map(str.lower, df.columns) 
    df.to_csv("data/pipeline/mdcm_barttovic_merged.csv")

    return df