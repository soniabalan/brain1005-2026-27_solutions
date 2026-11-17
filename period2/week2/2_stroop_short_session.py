"""
stroop_short_session.py  (BRAIN1005 Period 2, Practical 2)

The first 18 trials of one participant (sub-38, block 1) in a Stroop experiment.
Each trial is a dictionary; the whole session is a list of dictionaries.
rt_ms is the reaction time in milliseconds; correct is 1 (correct) or 0 (error).
"""

session = [
    {"trial": 1, "word": "DOG", "ink": "blue", "condition": "neutral", "response": "blue", "correct": 1, "rt_ms": 653},
    {"trial": 2, "word": "TABLE", "ink": "yellow", "condition": "neutral", "response": "yellow", "correct": 1, "rt_ms": 657},
    {"trial": 3, "word": "GREEN", "ink": "red", "condition": "incongruent", "response": "red", "correct": 1, "rt_ms": 651},
    {"trial": 4, "word": "RED", "ink": "blue", "condition": "incongruent", "response": "red", "correct": 0, "rt_ms": 712},
    {"trial": 5, "word": "RED", "ink": "red", "condition": "congruent", "response": "red", "correct": 1, "rt_ms": 663},
    {"trial": 6, "word": "WINDOW", "ink": "green", "condition": "neutral", "response": "green", "correct": 1, "rt_ms": 612},
    {"trial": 7, "word": "WINDOW", "ink": "green", "condition": "neutral", "response": "green", "correct": 1, "rt_ms": 922},
    {"trial": 8, "word": "BLUE", "ink": "red", "condition": "incongruent", "response": "red", "correct": 1, "rt_ms": 622},
    {"trial": 9, "word": "RED", "ink": "yellow", "condition": "incongruent", "response": "yellow", "correct": 1, "rt_ms": 944},
    {"trial": 10, "word": "YELLOW", "ink": "red", "condition": "incongruent", "response": "red", "correct": 1, "rt_ms": 819},
    {"trial": 11, "word": "CHAIR", "ink": "blue", "condition": "neutral", "response": "blue", "correct": 1, "rt_ms": 601},
    {"trial": 12, "word": "RED", "ink": "red", "condition": "congruent", "response": "red", "correct": 1, "rt_ms": 710},
    {"trial": 13, "word": "BLUE", "ink": "blue", "condition": "congruent", "response": "blue", "correct": 1, "rt_ms": 636},
    {"trial": 14, "word": "BLUE", "ink": "blue", "condition": "congruent", "response": "blue", "correct": 1, "rt_ms": 629},
    {"trial": 15, "word": "TABLE", "ink": "green", "condition": "neutral", "response": "green", "correct": 1, "rt_ms": 695},
    {"trial": 16, "word": "GREEN", "ink": "yellow", "condition": "incongruent", "response": "yellow", "correct": 1, "rt_ms": 904},
    {"trial": 17, "word": "YELLOW", "ink": "yellow", "condition": "congruent", "response": "yellow", "correct": 1, "rt_ms": 621},
    {"trial": 18, "word": "BLUE", "ink": "red", "condition": "incongruent", "response": "red", "correct": 1, "rt_ms": 835},
]

#%% Part 2

# initialise counts dict 
counts = {
    "congruent":0, 
    "incongruent":0,
    "neutral":0
    }
# loop over trials
for trial in session:
    # select condition from trial
    cdt = trial["condition"]
    # increase count
    if cdt in counts:
        counts[cdt] += 1

# ALTERNATIVE  initialise counts dict (will call it differently)
n_trials= {}
# loop over trials
for trial in session:
    # select condition from trial
    cdt = trial["condition"]
    # increase count for appropriate key
    n_trials[cdt] = n_trials.get(cdt, 0) + 1
        
# display result
print(counts)
print(n_trials)
        
#%%  Stroop effect in one participant
# for each condition, compute mean rt, nr of errors, interference effect

# initialise reaction time per condition dict
rt_condition = {
    "congruent":[], 
    "incongruent":[],
    "neutral":[]
    }
# initialise error count per condition dict
n_errors = {
    "congruent":0, 
    "incongruent":0,
    "neutral":0
    }
# loop over trials
for trial in session:
    # select condition from trial (just like in part 1)
    cdt = trial["condition"]
    corr = trial["correct"]
    # if correct trial, add rt, otherwise increase error count
    if corr == 1:
        rt_condition[cdt].append(trial["rt_ms"])
    else:
        n_errors[cdt] += 1
# print results as intermediate steps (I commented them out because the output is cleaner)        
#print(rt_condition)
#print(n_errors)

# calculate mean rt
mean_rt = {}
# loop over all items in rt dictionary
for cdt, values in rt_condition.items():
    # calculate mean
    mean_rt[cdt] = sum(values)/len(values)

# display mean RTs
print(f'Means (in miliseconds): {mean_rt}')

# calculate effect
interference = mean_rt["incongruent"] - mean_rt["neutral"]
facilitation = mean_rt["neutral"] - mean_rt["congruent"]

print(f'Interference effect: {interference:.2f} (ms) \nFacilitation effect: {facilitation:.2f} (ms)')

