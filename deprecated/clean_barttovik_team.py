import re
import pandas as pd

import warnings
from pandas.errors import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=(SettingWithCopyWarning))


def replace_non_numeric(value):
    try:
        if value:
            return float(value)
    except (ValueError, TypeError):
        return pd.NaT


def extract_between_parentheses(input_string):
    match = re.search(r"\((.*?)\)", str(input_string))
    if match:
        result = match.group(1)
        return result
    else:
        return input_string


def percent_str_to_float(value):
    if "%" in value:
        try:
            return float(value.rstrip("%")) / 100
        except (ValueError, AttributeError):
            return value
    else:
        return value


def clean_date(value):
    return value.split("\n")[0] if (value is not None and "\n" in value) else value


def clean_opp_rank(value):
    return value.split(" (")[0] if (value is not None and " (" in value) else value


def clean_barttovik_team(dfs: list[pd.DataFrame], team: str, year: int):

    # Loop Through Recieved Tables
    for i in range(len(dfs)):

        # Establish DF For Iteration
        df = dfs[i]
        cols_od = [
            "Category",
            "Offense_Val",
            "Offense_Rank",
            "Defense_Val",
            "Defense_Rank",
        ]
        cols_val_rank = ["Category", "Val", "Rank"]
        cols_conf = [
            "Category",
            "Non_Con_Val",
            "Non_Con_Rank",
            "Overall_Val",
            "Overall_Rank",
        ]

        # Team Stats Table
        if i == 0:
            # Remove Top Two Rows, Pick Out Rows and Columns of Interest
            df = df.iloc[2:]
            df_team_stats = pd.concat(
                [df.iloc[:5, :5], df.iloc[7:10, :5], df.iloc[12:14, :5]]
            )
            df_team_stats.columns = cols_od
            df_team_stats[cols_od[-4:]] = df_team_stats[cols_od[-4:]].applymap(
                replace_non_numeric
            )

            # Flatten Out Team Stats DataFrame
            df_team_stats_T = (
                pd.concat(
                    [df_team_stats.iloc[i] for i in range(len(df_team_stats))], axis=0
                )
                .to_frame()
                .T.drop(columns=["Category"])
            )
            df_team_stats_T.reset_index(drop=True, inplace=True)

            # Apply Proper Column Names
            df_team_stats_col = []
            for cat in df_team_stats["Category"]:
                df_team_stats_col.extend(list(cat + "_" + df_team_stats.columns[-4:]))
            df_team_stats_T.columns = df_team_stats_col
            df_team_stats = df_team_stats_T

        # Fun Stuff Table (Fortune/Failure Unexplained by Numbers)
        if i == 1:
            # Offensive/Defensive Efficiencies vs Quality Opponent & Last 10 Games
            df_team_fun_od = df.iloc[1:3, :5]
            df_team_fun_od.columns = cols_od
            df_team_fun_od_T = (
                pd.concat([df_team_fun_od.iloc[0], df_team_fun_od.iloc[1]], axis=0)
                .to_frame()
                .T.drop(columns=["Category"])
            )
            df_team_fun_od_T.columns = list(
                "Quality_Eff_" + df_team_fun_od.columns[-4:]
            ) + list("Last_10_" + df_team_fun_od.columns[-4:])

            # Performance In Close Games and In Quality Games
            df_team_fun_luck = df.iloc[3:6, :3]
            df_team_fun_luck.columns = cols_val_rank
            df_team_fun_luck[[cols_val_rank[1]]] = df_team_fun_luck[
                [cols_val_rank[1]]
            ].applymap(extract_between_parentheses)
            df_team_fun_luck_T = (
                pd.concat(
                    [
                        df_team_fun_luck.iloc[0],
                        df_team_fun_luck.iloc[1],
                        df_team_fun_luck.iloc[2],
                    ],
                    axis=0,
                )
                .to_frame()
                .T.drop(columns=["Category"])
            )
            df_team_fun_luck_T.columns = (
                list("Close_Games_" + df_team_fun_luck.columns[-2:])
                + list("Quality_Games_" + df_team_fun_luck.columns[-2:])
                + list("FUN_" + df_team_fun_luck.columns[-2:])
            )

            # Pct Of Games and Elite Team Would Lose With SoS (Non-Conference and Overall Schedule)
            df_team_fun_sos = df.iloc[8:10, :5]
            df_team_fun_sos.columns = cols_conf
            cols_conf_val_cols = [cols_conf[i] for i in [1, 3]]
            df_team_fun_sos[cols_conf_val_cols] = df_team_fun_sos[
                cols_conf_val_cols
            ].applymap(percent_str_to_float)
            df_team_fun_sos_T = (
                pd.concat([df_team_fun_sos.iloc[0], df_team_fun_sos.iloc[1]], axis=0)
                .to_frame()
                .T.drop(columns=["Category"])
            )
            df_team_fun_sos_T.columns = list(
                "Elite_L%_" + df_team_fun_sos.columns[-4:]
            ) + list("Pythag_Scheduled_Opp" + df_team_fun_sos.columns[-4:])

            # Concatenate The Transposed FUN Dataframes
            df_fun = pd.concat(
                [df_team_fun_od_T, df_team_fun_luck_T, df_team_fun_sos_T], axis=1
            )

        # Schedule Table
        if i == 2:
            # Drop First Two Rows, Reset Index, and Drop Uncessary Columns, Rename Columns
            df_schedule = (
                df.iloc[2:].reset_index(drop=True).drop(df.columns[[4, 10]], axis=1)
            )
            df_schedule.columns = [
                "Date",
                "Location",
                "Team_Rank",
                "Opponent_Rank",
                "Opponent",
                "Opponent_Short",
                "Result",
                "Tempo",
                "Record",
                "Wab",
                "AdjO",
                "AdjD",
                "Off_EFF",
                "Off_eFG%",
                "Off_TO%",
                "Off_OR%",
                "Off_FTR",
                "Off_2P",
                "Off_3P",
                "Def_EFF",
                "Def_eFG%",
                "Def_TO%",
                "Def_OR%",
                "Def_FTR",
                "Def_2P",
                "Def_3P",
                "Game_Score",
                "Avg_Lead_Deficit",
            ]

            # Clean The Data Column
            df_schedule["Date"] = df_schedule["Date"].apply(clean_date)
            df_schedule["Opponent_Rank"] = df_schedule["Opponent_Rank"].apply(
                clean_opp_rank
            )

            # Split Up Schedule And Add Regular, Conf Tourney, and NCAA Tourney
            null_indices = pd.concat(
                [
                    df_schedule[df_schedule["Opponent"].isnull()],
                    df_schedule[df_schedule["Opponent"] == "WAB"],
                ]
            ).index.tolist()
            df_schedule_reg = df_schedule.iloc[0 : null_indices[0]]
            df_schedule_reg["game_type"] = "regular_season"

            df_schedule_conf_tourney = df_schedule.iloc[
                null_indices[0] + 1 : null_indices[1]
            ]
            df_schedule_conf_tourney["game_type"] = "conference_tournament"

            df_schedule_ncaa_tourney = df_schedule.iloc[
                null_indices[1] + 1 : null_indices[2]
            ]
            df_schedule_ncaa_tourney["game_type"] = "ncaa_tournament"

            # Concatenate The Schedule DataFrame
            df_schedule = pd.concat(
                [df_schedule_reg, df_schedule_conf_tourney, df_schedule_ncaa_tourney]
            )

        if i == 4:
            print("oops")

    df_team_stats.to_csv(
        f"data/barttovik/{team}/barttovik_{team}_{str(year)}_team_stats.csv"
    )
    df_fun.to_csv(f"data/barttovik/{team}/barttovik_{team}_{str(year)}_fun.csv")
    df_schedule.to_csv(
        f"data/barttovik/{team}/barttovik_{team}_{str(year)}_schedule.csv"
    )

    return df_team_stats, df_fun, df_schedule
