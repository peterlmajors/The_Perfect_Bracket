# The Perfect Bracket

A feable attempt to accurately predict something with a roughly 1 in 120.2 billion chance of occuring.

# Overview
                                

This machine learning model leverages data spanning from 2008 to 2023 to approximate the probability of each possible
NCAA 2024 Men's College Basketball game. Each year, there are 67 games in the single elimination bracket. For each of these
games, we will measure our performance pre-game against betting lines and other prediction sites. Following each round, we will
evaluate game via metrics such as Brier score and log loss. </p2>

# How To Use

* (1) Clone repo to your local machine and ensure you have all Python packages in the requirements.txt folder.
* (2) Manually download scripts from this [Kaggle](https://www.kaggle.com/datasets/nishaanamin/march-madness-data) dataset, which are listed in kaggle_download.txt.
* (3) Run the <b> main.py </b> to populate and clean barttovic data and perform remaining necessary steps.
* (4) Inspect terminal during runtime to follow progression of the worklow.
* (5) Once complete, open <b> predictions.csv </b> and <b> performance.csv </b> and profit!

# Top Level Folders

<h2> Python (.py) Workflow </h2>
                                                  
<b> API (Level 2): </b> <p2> Scripts for accessing data and saving to local machine via the cbbdata library in R. This library retrieves advanced statsitics
                and box scores from Barttovik, ESPN, Kenpom, and various college baskebtall resources. </p2>

<b> Processing (Level 2): </b> <p2> Reusable functions for completing smaller steps in the data pipeline. These scripts perform variety of tasks, including 
                merging, preprocessing, training, and predicting on the current year's tournament data. </p2>

<b> Pipeline: (Level 1): </b> <p2> Each file contains function calls relevant to a larger step in the end-to-end workflow. These scripts call functions in 
                the procesing folder and themself are called in the main.py script. This allows for functions to be repurposed for the Men's and Women's 
                brackets, as well as for their feeder models. </p2>

<b> Main: (Level 0): </b> <p2> Calls the pipeline scripts as subprocesses to run the end-to-end pipeline with maximum visiblity and flexibility. </p2>
                    
<b> Exploration: </b> <p2> Jupyter notebooks used during the model training and development process. </p2>

<b> Deprecated: </b> <p2> Scripts previously used to scrape, clean, and merge barttovik data before being replaced by the cbbdata. </p2> 

<b> Sample: </b> <p2> Submissions gathered from other researchers' March Madness prediction competitions. </p2> 

<h2> Jupter Notebook (.ipynb) Workflow </h2>

<b> submission.ipynb: </b> <p2> Jupyter notebook to be uploaded to Kaggle for the 'March Machine Learning Mania 2024' code competition. This contains all the logic
                  to run the pipeline end-to-end, which also split up into different .py files for maintainability. </p2>

<h2> Supporting Documents (.csv) </h2>

<b> Data: </b> <p2> Contains folders for data that is acquired on runtime (cbbdata), must be provided (kaggle, mdcm), and is produced on runtime (pipeline). So long as
                you have an account with cbbdata (as explained in api/cbbdata.R), you can retreive this data by running main. In the kaggle folder, the march_madness_data
                can be found at the following [link](https://www.kaggle.com/datasets/nishaanamin/march-madness-data), while the data in march_machine_learning_mania can only
                be accessed on the competition [page](https://www.kaggle.com/competitions/march-machine-learning-mania-2024). Data in the mdcm folder contains historical 
                tournament game results and team spellings, and can only be accessed by emailing peterlmajors@gmail.com. The pipeline folder is populated on runtime. </p2>
