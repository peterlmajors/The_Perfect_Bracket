# Import Packages
import pandas as pd
from os import walk
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.acquire_barttovik import export_barttovic 
from processing.clean_barttovic_trank import clean_barttovic_trank
from processing.merge_barttovic_trank import merge_barttovic_trank

# Define Common Variables ----------------------------------------------------------------------------------
years = list(range(2008, 2025))

# Create TRank Folder
if not os.path.exists(f'data/barttovic/trank'):
    os.makedirs(f'data/barttovic/trank')
    created =+ 1

# Scrape, Clean, and Download Home Page (TRank) To .csv -----------------------------------------------------

print("\nScraping and Cleaning ------------------\n")

for year in years:
    if (f'barttovic_trank_{str(year)}.csv' not in next(walk('data/barttovic/trank'), (None, None, []))[2]) or (year == 2024):
        scraped_df = export_barttovic(f'https://barttorvik.com/trank.php?year={year}&sort=&top=0&conlimit=All#')
        print(f"Scrape complete for {year} TRank.")
        clean_barttovic_trank(scraped_df, year)
        print(f"Cleaning complete for {year} TRank.\n")
    else:
        print(f"Already scraped and cleaned TRank for {year}.\n")    
        
# Merge Onto Existing Historical Data -----------------------------------------------------------------------

print("\nData Merging ---------------------------\n")

df = merge_barttovic_trank(pd.read_csv('data/mdcm/NCAA_Tourney_2002_2023.csv'), years[:-1])
