
# Import Libraries
# install.packages("rlang")

library("devtools")
# library("cbbdata")
# try(cbd_torvik_current_resume())

#Load Package-----
library(hoopR)
library(ncaahoopR)

#Download PBP Data-----

#ESPN Teams Data
espn_teams <- espn_mbb_teams()

#ESPN Team Box 
espn_team_bx <- load_mbb_team_box(seasons = most_recent_mbb_season())

#ESPN PBP
espn_pbp <- load_mbb_pbp(seasons = most_recent_mbb_season())

#Total Ids
team_ids <- data(ids)

write.csv(espn_teams, 'C:/Users/Peter/Python Scripts/Case Competitions/MDCM 2023/teams.csv')

install.packages("ncaahoopR")
