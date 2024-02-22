# Import Packages
import pandas as pd
from os import walk
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.acquire_barttovik import export_barttovic 

# Define Common Variables ----------------------------------------------------------------------------------
years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
teams = ['Houston']

# Create Folders For All Teams
created, existing = 0, 0
for team in teams:
    if not os.path.exists(f'data/barttovic/{team}'):
        os.makedirs(f'data/barttovic/{team}')
        created =+ 1
    else:
        existing =+1
    print(f"\n{existing} team folders checked and {created} created.\n")

# Scrape and Download Team Pages From Listed Years To .csv -----------------------------------------------------

# print("\nWeb Scraping --------------\n")
# for year in years:
#     if (f'barttovic_Houston_{str(year)}.csv' not in next(walk('data/barttovic/Houston'), (None, None, []))[2]) or (year == 2024):
#         export_barttovic(f'https://barttorvik.com/team.php?team=Houston&year={year}', str("barttovic_Houston_" + str(year)))
#         print(f"Scrape complete for {year} Houston.")
#     else:
#         print(f"Already scraped for {year} Houston.")    

