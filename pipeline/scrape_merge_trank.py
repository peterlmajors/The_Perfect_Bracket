# Script To Scrape Data From Barttovic and Merge Onto MDCM Data

# This sript scrapes Barttovic tranks from 2008 to 2024, writes them into data/barttovic, reads them from memory, cleans them
# according to the pipeline's needs, writes them back into data/barttovic, reads them again to merge onto NCAA_Tourney_2002_2023.csv, 
# and finally exports a new mdcm_barttovic_merged.csv file. Script should be run if the barttovic files do not exist on your local machine 
# or if you'd like to update the current year's trank data. 

# Import Packages
import pandas as pd
from os import walk

from api.acquire_barttovik import export_barttovic
from processing.clean_barttovic import clean_barttovic
from processing.merge_barttovic import merge_barttovic

# Define Common Variables ----------------------------------------------------------------------------------
years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Scrape and Download Home Page (TRank) To .csv -----------------------------------------------------

print("\nWeb Scraping --------------\n")
for year in years:
    if (f'barttovic_trank_{str(year)}.csv' not in next(walk('data/barttovic'), (None, None, []))[2]) or (year == 2024):
        export_barttovic(f'https://barttorvik.com/trank.php?year={year}&sort=&top=0&conlimit=All#', str("barttovic_trank_" + str(year)))
        print(f"Scrape complete for {year} TRank.")
    else:
        print(f"Already scraped TRank for {year}.")    

# Clean Home Page (TRank) -----------------------------------------------------------------------------------

# print("\nData Cleaning -------------\n")
# for year in years:
#     if (pd.read_csv(f'data/barttovic/barttovic_trank_{year}.csv').iloc[1,2] == "Team") or (year == 2024):
#         clean_barttovic(year)  
#         print(f"Cleaning complete for {year} TRank.")
#     else:
#         print(f"Already cleaned TRank for {year}.")    
    
# Merge Onto Existing Historical Data -----------------------------------------------------------------------

# print("\nData Merging --------------\n")

# if not os.path.exists('data/pipeline/mdcm_barttovic_merge.csv') or (year == 2024):
#     df = merge_barttovic(pd.read_csv('data/mdcm/NCAA_Tourney_2002_2023.csv'), years[:-1])
#     print("Barttovic TRank and MDCM data merge complete.\n")
# else:
#     print("Barttovik TRank and MDCM data merge already complete.\n")