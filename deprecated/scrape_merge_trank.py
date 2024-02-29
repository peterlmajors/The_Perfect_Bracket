# This sript scrapes barttovik tranks from 2008 to 2024, writes them into data/barttovik, cleans them according to the pipeline's
# needs, writes them into data/barttovik, reads them again to merge onto NCAA_Tourney_2002_2023.csv, and finally exports a new
# mdcm_barttovik_merged.csv file. Script should be run if the barttovik files do not exist on your local machine or if you'd
# like to update the current year's trank data.

# Import Packages
import pandas as pd
from os import walk
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from deprecated.acquire_barttovik import export_barttovik
from deprecated.clean_barttovik_trank import clean_barttovik_trank
from processing.merge_barttovik_trank import merge_barttovik_trank

# Define Common Variables ----------------------------------------------------------------------------------
years = [year for year in range(2008, 2025) if year != 2020]

# Create TRank Folder
if not os.path.exists(f"data/barttovik/trank"):
    os.makedirs(f"data/barttovik/trank")
    created = +1

# Scrape, Clean, and Download Home Page (TRank) To .csv -----------------------------------------------------

print("\nScraping and Cleaning ------------------\n")

for year in years:
    if (
        f"barttovik_trank_{str(year)}.csv"
        not in next(walk("data/barttovik/trank"), (None, None, []))[2]
    ) or (year == 2024):
        # Scrape For The Year
        scraped_df = export_barttovik(
            f"https://barttorvik.com/trank.php?year={year}&sort=&top=0&conlimit=All#"
        )[0]
        print(f"Scrape complete for {year} TRank.")
        # Clean For The Year
        clean_barttovik_trank(scraped_df, year)
        print(f"Cleaning complete for {year} TRank.\n")
    else:
        print(f"Already scraped and cleaned TRank for {year}.\n")

# Merge Onto Existing Historical Data -----------------------------------------------------------------------

print("\nData Merging ---------------------------\n")

df = merge_barttovik_trank(
    pd.read_csv("data/mdcm/NCAA_Tourney_2002_2023.csv"), years[:-1]
)
