# Main Script To Output Most Up-To-Date 2024 March Madness Predictions

# Import Packages
import subprocess

# Script To Scrape & Clean Data From CBB Data API in R ---------------------------------------------------------------

subprocess.call(['C:/Program Files/R/R-4.3.2/bin/Rscript', '--vanilla', 'api/cbb_data.r'], shell = True)
