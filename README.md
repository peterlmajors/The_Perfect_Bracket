# The Perfect Bracket

A feable attempt to accurately predict something with a roughly 1 in 120.2 billion chance of occuring.

# Overview

This machine learning model leverages data spanning from 2008 to 2023 to approximate the probability of each possible 
NCAA 2024 Men's College Basketball game. Each year, there are 67 games in the single elimination bracket. For each of these
games, we will measure our performance pre-game against betting lines and post-game via metrics such as Brier score. </p2>
q
<h2> API: </h2> <p2> Scripts for accessing data and saving to local machine. This model retrieves data from [Barttovic](https://barttorvik.com/#),
                which hosts free Kenpom-esque team and player-level college basketball statistics. </p2>

<h2> Pipeline: </h2> <p2> File contains function calls to complete steps of interest in the data pipeline. Scripts are called in order by the main. </p2>

<h2> Processing: </h2> <p2> Each file contains a function relevant to a step in the data pipeline. Functions called by scripts in the pipeline folder. </p2>
