# Import Packages
import re
import pandas as pd

def clean_barttovic_trank(df: pd.DataFrame, year: str):
    try:
        # Drop First Few Columns and Rows, Column Headers 
        df.columns = df.iloc[1]
        df = df.iloc[2:, 1:]
        
        # Remove Rows With "Team" as Row (Headers)
        df = df[~df['Team'].str.contains('Team')] 
        
        # Remove Non Team Name Part of String
        df['Team'] = df['Team'].str.split('(').str[0]
        
        # Remove Final Result In Tournament
        pattern = "|".join(map(re.escape, ['1 seed', '2 seed', '3 seed', '4 seed', '5 seed', '6 seed', '7 seed', '8 seed', 
                                           '9 seed', '10 seed', '11 seed', '12 seed', '13 seed', '14 seed', '15 seed', '16 seed']))
        def split_string(s):
            parts = re.split(pattern, s)
            return [part.strip() for part in parts if part][0]
        df['Team'] = df['Team'].apply(lambda x: split_string(x))
        
        # Align Team Names With Those From MDCM Data, Create Team_Season ID
        team_mapping = {'Abilene Christian': 'Abilene Chr','Alabama St.': 'Alabama St','Albany': 'Albany NY','American': 'American Univ','Appalachian St.': 'Appalachian St',
                        'Arizona St.': 'Arizona St','Little Rock': 'Ark Little Rock','Arkansas Pine Bluff': 'Ark Pine Bluff','Boise St.': 'Boise St','Boston University': 'Boston Univ',
                        'Cal St. Bakersfield': 'CS Bakersfield','Cal St. Fullerton': 'CS Fullerton','Cal St. Northridge': 'CS Northridge','Cal Poly': 'Cal Poly SLO','Cleveland St.': 'Cleveland St',
                        'Coastal Carolina': 'Coastal Car','College of Charleston': 'Col Charleston','Colorado St.': 'Colorado St','Coppin St.': 'Coppin St','Eastern Kentucky': 'E Kentucky',
                        'Eastern Washington': 'E Washington','East Tennessee St.': 'ETSU','Fairleigh Dickinson': 'F Dickinson','Florida Atlantic': 'FL Atlantic','Florida Gulf Coast': 'FL Gulf Coast',
                        'Florida St.': 'Florida St','Fresno St.': 'Fresno St','George Washington': 'G Washington','Georgia St.': 'Georgia St','Indiana St.': 'Indiana St','Iowa St.': 'Iowa St',
                        'Jacksonville St.': 'Jacksonville St','Kansas St.': 'Kansas St','Kennesaw St.': 'Kennesaw','Kent St.': 'Kent','Long Beach St.': 'Long Beach St','LIU Brooklyn': 'Long Island',
                        'Loyola Chicago': 'Loyola-Chicago','Mississippi Valley St.': 'MS Valley St','Middle Tennessee': 'MTSU','Michigan St.': 'Michigan St','Mississippi St.': 'Mississippi St',
                        'Montana St.': 'Montana St','Morehead St.': 'Morehead St','Morgan St.': 'Morgan St',"Mount St. Mary's": "Mt St Mary's",'Murray St.': 'Murray St','Northern Colorado': 'N Colorado',
                        'North Dakota St.': 'N Dakota St','Northern Kentucky': 'N Kentucky','North Carolina A&T': 'NC A&T','North Carolina Central': 'NC Central','North Carolina St.': 'NC State',
                        'New Mexico St.': 'New Mexico St','Norfolk St.': 'Norfolk St','Northwestern St.': 'Northwestern LA','Ohio St.': 'Ohio St','Oklahoma St.': 'Oklahoma St','Oregon St.': 'Oregon St',
                        'Penn St.': 'Penn St','Portland St.': 'Portland St','Prairie View A&M': 'Prairie View','South Dakota St.': 'S Dakota St','Southeast Missouri St.': 'SE Missouri St',
                        'Stephen F. Austin': 'SF Austin','Sam Houston St.': 'Sam Houston St','San Diego St.': 'San Diego St','UC Santa Barbara': 'Santa Barbara','Southern': 'Southern Univ',
                        'St. Bonaventure': 'St Bonaventure',"St. John's": "St John's","Saint Joseph's": "St Joseph's PA",'Saint Louis': 'St Louis',"Saint Mary's": "St Mary's CA",
                        "Saint Peter's": "St Peter's",'Texas A&M Corpus Chris': 'TAM C. Christi','Texas Southern': 'TX Southern','Louisiana Lafayette': 'ULL','UTSA': 'UT San Antonio',
                        'Utah St.': 'Utah St','VCU': 'VA Commonwealth','Western Kentucky': 'W Kentucky','Western Michigan': 'W Michigan','Green Bay': 'WI Green Bay',
                        'Milwaukee': 'WI Milwaukee','Washington St.': 'Washington St','Weber St.': 'Weber St','Wichita St.': 'Wichita St','Wright St.': 'Wright St'}
        
        df['Team'] = df['Team'].replace(team_mapping) 
        df['team_season'] = df['Team'] + "_" + str(year)
        
        df.to_csv(f'data/barttovic/trank/barttovic_trank_{str(year)}.csv')
     
    except Exception as e: 
        print("Error Encountered In Data Cleaning. Details: ", e)