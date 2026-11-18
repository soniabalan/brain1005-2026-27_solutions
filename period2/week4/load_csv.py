"""Prepare the participant-level data for Tutorial 4."""

import csv
from pathlib import Path
from statistics import mean, stdev 
# importing some libraries to handle the data


def load_csv():
    """Load the summary CSV next to this module and prepare plotting data."""
    # this makes sure to read the correct file from the correct folder
    root = Path(__file__).resolve().parent # pick folder
    summary = root / "summary_by_participant.csv" # pick file
    
    # prepare dictionary elements
    keys = ["congruent", "neutral", "incongruent"]
    conditions = ["Congruent", "Neutral", "Incongruent"]

    # same as in week 3, we open a file and use DictReader to save the data in a dictionary
    with summary.open(newline="", encoding="utf-8-sig") as file:
        rt_rows = [
            [float(row[f"mean_rt_{key}"]) for key in keys]
            for row in csv.DictReader(file)
        ]

    # get some summary statistics using some fancy python syntax, the specifics don't matter rn
    congruent, neutral, incongruent = map(list, zip(*rt_rows)) 
    n = len(rt_rows)
    mean_rts = [mean(values) for values in zip(*rt_rows)] 
    sd_rts = [stdev(values) for values in zip(*rt_rows)]
    interference = [i - n_rt for _, n_rt, i in rt_rows]
    facilitation = [n_rt - c for c, n_rt, _ in rt_rows]
    positive = [i > 0 for i in interference]
    
    # return statement !!! the function saves the folllowing vairables (in order)
    return conditions, mean_rts, sd_rts, interference, facilitation, positive
