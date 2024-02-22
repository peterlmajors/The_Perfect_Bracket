# Main Script To Output Most Up-To-Date 2024 March Madness Predictions

# Import Packages
import subprocess

# Script To Scrape & Clean Data From Barttovic and Merge Onto MDCM Data ---------------------------------------------------------------

# This sript scrapes Barttovic tranks from 2008 to 2024, writes them into data/barttovic, cleans them according to the pipeline's 
# needs, writes them into data/barttovic, reads them again to merge onto NCAA_Tourney_2002_2023.csv, and finally exports a new
# mdcm_barttovic_merged.csv file. Script should be run if the barttovic files do not exist on your local machine or if you'd 
# like to update the current year's trank data. 

subprocess.run(["python", 'pipeline/scrape_merge_trank.py'])
