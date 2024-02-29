# Import Packages
import pandas as pd
from os import walk
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from deprecated.acquire_barttovik import export_barttovik
from deprecated.clean_barttovik_team import clean_barttovik_team

# Define Common Variables ----------------------------------------------------------------------------------
years = [year for year in range(2008, 2025) if year != 2020]
teams = ["Houston"]

# Create Folders For All Teams
created, existing = 0, 0
for team in teams:
    if not os.path.exists(f"data/barttovik/{team}"):
        os.makedirs(f"data/barttovik/{team}")
        created = +1
    else:
        existing = +1
    print(f"\n{existing} team folders checked and {created} created.\n")

# Scrape and Download Team Pages From Listed Years To .csv -----------------------------------------------------

print("\nWeb Scraping --------------\n")
for team in teams:
    for year in years:
        if (
            f"barttovik_{team}_{str(year)}.csv"
            not in next(walk(f"data/barttovik/{team}"), (None, None, []))[2]
        ) or (year == 2024):
            # Scrape For Team Year
            scraped_dfs = export_barttovik(
                f"https://barttorvik.com/team.php?team={team}&year={year}",
                str(f"barttovik_{team}_" + str(year)),
            )
            print(f"Scrape complete for {year} {team}.")
            # Clean For Team Year
            clean_barttovik_team(scraped_dfs, year)
            print(f"Scrape complete for {year} {team}.")
        else:
            print(f"Already scraped and cleaned for {year} {team}.")
