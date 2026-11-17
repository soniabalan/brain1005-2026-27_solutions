
"""
Reading and writing data from a file (with some data manipulation/cleaning in between)

COMMENTS GIVE A BIT MORE EXPLANATION THIS TIME, DON'T SKIP THEM
"""
# Setup
import csv 
import os

# NOTE: Make sure your script is in the same folder as "data" folder
print(os.getcwd())
print("Checking if files are accessible: ")
print("data" in os.listdir()) # expected: True

#%% Functions

def load_participant(filename):
    """Return a list of trial dictionaries."""
    # from the lecture, copy pasted
    with open(filename) as f:
        trials = list(csv.DictReader(f))
    return trials

def is_valid(trial):
    """True if the trial is neither a miss nor an anticipation."""
    # check if there is a response
    if trial["response"] == "none":
        return False
    # return (keep) only trials without anticipation
    return float(trial["rt_ms"]) >= 150

def summarize(trials):
    """Mean RT and accuracy per condition, valid trials only."""
    
    # initialise some lists/dicts
    n_condition = {} # counts nr of trials ni each condition
    n_correct = {} # counts nr of CORRECT trials in each condition
    rt_condition = {} # add rt per condition
    summary = {} # summary (mean rt and accuracy per condition, interferrence and facilitation)
    
    # loop over trials
    for trial in trials:
        # only for valid trials
        if is_valid(trial):
            # select condition from trial
            cdt = trial["condition"]
            corr = int(trial["correct"])
            # same as week 2 - increase count by 1
            n_condition[cdt] = n_condition.get(cdt,0) + 1
            # if correct trial, add rt and increase correct count
            if corr == 1:
                # same as week 2 - update values correspondingly
                rt_condition[cdt] = float(rt_condition.get(cdt, 0)) + float(trial["rt_ms"])
                n_correct[cdt] = n_correct.get(cdt,0) + 1
     

    # loop over all conditions in rt dictionary
    for cdt, total_rt in rt_condition.items():
        # calculate means, and accuracy, arranged in such a way to make sense for last ex
        summary[f"mean_rt_{cdt}"] = round(total_rt/n_condition[cdt],2)
        summary[f"accuracy_{cdt}"] = round(n_correct[cdt]/n_condition[cdt],2)
        
        
    # adding interferrence and facilitation just to show you that you can    
    summary["interferrence"] = round(summary["mean_rt_incongruent"] - summary["mean_rt_neutral"],2)
    summary["facilitation"] = round(summary["mean_rt_neutral"] - summary["mean_rt_congruent"],2)
    
    # save summary as an output of the function
    return summary

#%% CALLING FUNCTIONS - above, we are just defining them, we call them here, meaning we actually give values to the parameters
''' For just one participant '''

participant_test = load_participant("data/sub-03_stroop.csv")
summary_test = summarize(participant_test)

#%%
''' For all participants '''
# initialise variables
data = [] # to store all the data
data_summary = [] # to store participant summary
participant_id = 1 # participant ID

# loop over all files in the "data" folder
for filename in os.listdir("data"):
    # load participant
    participant = load_participant(f"data/{filename}")
    # append data 
    data.append(participant)
    
    # to data and summary to data_summary
    summary = summarize(participant)
    # add participant_id key
    summary["participant_id"] = participant_id
    data_summary.append(summary)
    # increase participat ID for next file (next participant)
    participant_id += 1


#%% Save data into a csv file
columns = [
    "participant_id",
    "mean_rt_congruent", 
    "accuracy_congruent",
    "mean_rt_neutral", 
    "accuracy_neutral",
    "mean_rt_incongruent", 
    "accuracy_incongruent",
    "interferrence",
    "facilitation"
    ]

# from lecture, copy pasted
# NOTE: Make sure you make a folder called "results" in the same folder as "data"
with open("results/summary.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=columns) 
    writer.writeheader()
    writer.writerows(data_summary) # <-- a dict. variable 

#%% Average interferrence 
total_interferrence = 0
total_facilitation = 0
for participant in data_summary: 
    total_interferrence += participant["mean_rt_incongruent"] - participant["mean_rt_neutral"]
    total_facilitation += participant["mean_rt_neutral"] - participant["mean_rt_congruent"]
    
total_facilitation = total_facilitation/len(data_summary)
total_interferrence = total_interferrence/len(data_summary)

print(f"The overall group interferrence effect is: {total_interferrence:.2f}")
print(f"The overall group facilitation effect is: {total_facilitation:.2f}")

# check -- doing this just to show you that there are multiple ways to arrive at the same conclusion, and they are all good options
total_interferrence = 0
total_facilitation = 0
for participant in data_summary: 
    total_interferrence += float(participant["interferrence"])
    total_facilitation += float(participant["facilitation"])

total_facilitation = total_facilitation/len(data_summary)
total_interferrence = total_interferrence/len(data_summary)

print(f"The overall group interferrence effect is: {total_interferrence:.2f} (using scores computed in summarize())")
print(f"The overall group facilitation effect is: {total_facilitation:.2f} (using scores computed in summarize())")

# this is good to check that the program is actually doing what you want it to do (which is different than it running without errors)
print("If you go to your output file, to the [interferrence] and [facilitation] columns that I added")
print("you will find interferrence ~ 50.04, and facilitation ~ 13.10")

