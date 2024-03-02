# Load Common Libraries -----------------------------------------------------
library(tidyverse)

# Install cbbdata (If Installed, Just Load In) ------------------------------
if (!requireNamespace("cbbdata", quietly = TRUE)) {
  library(devtools)
  devtools::install_github("andreweatherman/cbbdata")
  library("cbbdata", character.only = TRUE)
  cat(paste("\nPackage", "cbbdata", "installed and loaded.\n"))
} else {
  library("cbbdata", character.only = TRUE)
  cat(paste("\nPackage", "cbbdata", "already installed and loaded.\n"))
}

# Login To cbbdata ----------------------------------------------------------

# If you don't have a cbd account, uncomment and replace strings with your info.
# cbbdata::cbd_create_account("USERNAME", "EMAIL", "PASSWORD", "PASSWORD")  # nolint
# This will send you an email with an API key and allow you to use cbd_login()

# Once you have an account, login with your credentials stored in .env
readRenviron(".env")
username <- Sys.getenv("CBD_USER")
password <- Sys.getenv("CBD_PW")
cbbdata::cbd_login(username, password)

# Establish Variables -------------------------------------------------------
years <- seq(2008, 2024)
years <- years[years != 2020]

# Define Functions ----------------------------------------------------------

# Export .csv Files To data/cbbdata Folder
export_to_data <- function(df, file, subfolder){
    folder_path <- file.path("data", "cbbdata", subfolder)
    # Create Folder If Does't Exist and Write To It
    if (!dir.exists(folder_path)) {
        dir.create(folder_path)
        print(paste(folder_path, "created."))}
    write.csv(df, file.path(folder_path, file), row.names = FALSE)
    print(paste("Successfully exported to: ", file.path(folder_path, file)))
}

# Export Conference Factors -------------------------------------------------

all_conf_factors <- tibble()
for (i in years) {
  year_conf_factors <- cbbdata::cbd_torvik_conf_factors(year = i)
  print(paste("Acquired NCAA Men's Conference Statistcs for", as.character(i)))
  all_conf_factors <- bind_rows(all_conf_factors, year_conf_factors)
}
export_to_data(all_conf_factors, file = "conference_factors.csv", "conference")

# Export Box Scores ---------------------------------------------------------

export_to_data(cbbdata::cbd_torvik_game_box(), file = "box_scores.csv", "game")

# Export Team Ratings By Day -----------------------------------------------

export_to_data(cbbdata::cbd_torvik_ratings_archive(), file = "team_ratings.csv", 'team')

# Export Current Resume -----------------------------------------------------

export_to_data(cbbdata::cbd_torvik_current_resume(), file = "team_resume.csv", "current")

# Export Game Stats ---------------------------------------------------------

export_to_data(cbbdata::cbd_torvik_game_stats(), file = "game_stats.csv", "game")

# Export Game Factors -------------------------------------------------------

export_to_data(cbbdata::cbd_torvik_game_factors(), file = "game_factors.csv", "game")

# Export Player Game Peformance ---------------------------------------------

export_to_data(cbbdata::cbd_torvik_player_game(), file = "player_game.csv", "player")

# Export Player Season Peformance -------------------------------------------

export_to_data(cbbdata::cbd_torvik_player_season(), file = "player_season.csv", "player")

# Export Player Game Peformance ---------------------------------------------

export_to_data(cbbdata::cbd_torvik_player_split(split = 'game_type'), file = "player_split.csv", "player")

# Export Selection Sunday Resume --------------------------------------------

export_to_data(cbbdata::cbd_torvik_resume_database(n = 1500, min_year = 2008, max_year = 2024, max_net = 80), file = "selection_sunday_resume.csv", "team")

# Export NCAA Seeding Comittee Sheets ---------------------------------------
# Evaluate Mismatched Seeding Against The Comittee's Own Standards!
# Official Data Only Exists For 2019, 2021, 2022, and 2023

all_ncaa_sheets <- tibble()
years <- seq(2019, 2024)
years <- years[years != 2020]

for (i in years) {
  year_ncaa_sheets <- cbbdata::cbd_torvik_ncaa_sheets(year = i)
  year_ncaa_sheets <- year_ncaa_sheets %>% mutate(year = i)
  print(paste("Acquired NCAA Evaluators Sheets for", as.character(i)))
  all_ncaa_sheets <- bind_rows(all_ncaa_sheets, year_ncaa_sheets)
}
export_to_data(all_ncaa_sheets, file = "ncaa_sheets.csv", "ncaa_sheet")

# Export Current Projections ------------------------------------------------
# Compare Final Predictions For Men's Bracket To ESPN's, Additional Validation

export_to_data(cbbdata::cbd_bpi_ratings(), file = "current_resume.csv", "current")
