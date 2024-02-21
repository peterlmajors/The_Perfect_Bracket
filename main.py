# Main Script To Output Most Up-To-Date 2024 March Madness Predictions

# Import Packages
import subprocess

# Scrape Data From Barttovic and Merge Onto MDCM Data 
subprocess.run(["python", 'pipeline/scrape_merge_trank.py'])