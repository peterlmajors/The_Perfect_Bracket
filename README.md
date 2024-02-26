# The Perfect Bracket

A feable attempt to accurately predict something with a roughly 1 in 120.2 billion chance of occuring.

# Overview
                                

This machine learning model leverages data spanning from 2008 to 2023 to approximate the probability of a team win each possible NCAA 2024 Men's College Basketball game. 
Each year, there are 67 games in the single elimination bracket. For each of these games, we will measure our performance pre-game against betting lines and post-game via
metrics such as Brier score. Scripts and functions are placed into folders and follow the structure in the 'Workflow' section of Top Level Folders. </p2>

# How To Use

* (1) Clone repository to your local machine and ensure you have all Python packages in the requirements.txt folder.
* (2) Manually download scripts from this [Kaggle](https://www.kaggle.com/datasets/nishaanamin/march-madness-data) dataset, which are listed in kaggle_download.txt.
* (3) Run the <b> main.py </b> to populate and clean barttovic data and perform remaining necessary steps.
* (4) Inspect terminal during runtime to follow progression of the worklow.
* (5) Once complete, open <b> predictions.csv </b> and <b> performance.csv </b> and profit!

# Top Level Folders

<h2> Workflow </h2>
                                                                      
<b> API (Level 2): </b> <p2> Reusable functions for accessing data and saving to local machine. They use BeatifulSoup4 to scrape from [Barttovic](https://barttorvik.com/#),
                which hosts team and player-level college basketball statistics, as well as [CBB Ref](https://pypi.org/project/CBBpy/) which serves a similar purpose.

<b> Processing (Level 2): </b> <p2> Reusable functions for completing smaller steps in the data pipeline. These scripts perform variety of tasks, including but not limited to 
                pulling, cleaning, merging, storing, preprocessing, training, and predicting on the current year's tournament. </p2>

<b> Pipeline: (Level 1): </b> <p2> Each file contains function calls relevant to a larger step in the end-to-end workflow. These scripts call functions in the procesing folder 
                and themself are called in the main.py script. </p2>
                
<b> Main: (Level 0): </b> <p2> Calls the pipeline scripts as subprocesses to run the end-to-end pipeline with maximum visiblity and flexibility. </p2>

<h2> Supporting </h2>

<b> Data: </b> <p2> Contains folders for data which must be scraped from barttovic (trank & each team), data which must be downloaded from this public 
              [Kaggle](https://www.kaggle.com/datasets/nishaanamin/march-madness-data) dataset, and data which is already contained in this repository. </p2>
              
<b> Exploration: </b> <p2> Jupyter notebooks used to test models and develop code during the development process. Not called by workflow. </p2>
              
