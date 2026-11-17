#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 2026

@author: administrator

BRAIN1005 - Programming I - Period 2, Lecture 2: Dictionaries & Tuples
Run cell by cell in Spyder. Each cell matches one slide.
Some cells are meant to fail: read the error, then move on to the next cell.
"""

#%% The session we use today
# The first 18 trials of one participant (sub-38, block 1) in the Stroop task.
# Each trial is a dictionary; the whole session is a list of dictionaries.
# This is the same session you will use in Practical 2 (stroop_short_session.py).
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

#%% The problem with positions
# One trial as a list: you have to remember what each position means
trial_list = [3, "GREEN", "red", "incongruent", "red", 1, 651]
trial_list[6]       # → 651   (but what is 651?)
trial_list[5]       # → 1     (trial number? correct? block?)

# The same trial as a dictionary: every value carries its name
trial = {"trial": 3, "word": "GREEN", "ink": "red", "condition": "incongruent",
         "response": "red", "correct": 1, "rt_ms": 651}
trial["rt_ms"]      # → 651
trial["correct"]    # → 1

#%% Anatomy of a dictionary
trial = {"word": "GREEN", "ink": "red", "rt_ms": 651}

type(trial)         # → <class 'dict'>
len(trial)          # → 3   (three key-value pairs)
trial               # → {'word': 'GREEN', 'ink': 'red', 'rt_ms': 651}

empty = {}
len(empty)          # → 0

#%% Looking up a value
trial = {"word": "GREEN", "ink": "red", "rt_ms": 651}

trial["ink"]        # → 'red'
trial["rt_ms"]      # → 651

#%% Looking up a value - the error: a key that does not exist
trial["RT"]
# → KeyError: 'RT'
# keys are case-sensitive and must match exactly

#%% Looking up a value - the error: there are no positions
trial[0]
# → KeyError: 0
# a dictionary is looked up by key, not by position

#%% A dictionary as a lookup table
# The participant presses one of four keys; each key stands for a color
key_to_color = {"d": "red", "f": "green", "j": "blue", "k": "yellow"}

key_to_color["j"]   # → 'blue'

# Translate the first five key presses of the session
presses = ["j", "k", "d", "d", "d"]
responses = []
for key in presses:
    responses.append(key_to_color[key])
print(responses)    # → ['blue', 'yellow', 'red', 'red', 'red']

#%% Adding and updating entries
trial = {"word": "GREEN", "ink": "red", "rt_ms": 651}

trial["condition"] = "incongruent"   # new key -> added
trial["rt_ms"] = 655                 # existing key -> replaced
print(trial)
# → {'word': 'GREEN', 'ink': 'red', 'rt_ms': 655, 'condition': 'incongruent'}

len(trial)          # → 4

#%% Adding and updating - keys are unique
# Writing the same key twice keeps only the last value, without any warning
trial = {"ink": "red", "ink": "blue"}
print(trial)        # → {'ink': 'blue'}

#%% Is the key there? in and get()
trial = {"word": "GREEN", "ink": "red", "rt_ms": 651}

"rt_ms" in trial            # → True
"accuracy" in trial         # → False
"red" in trial              # → False  (in looks at keys, not values)

trial.get("rt_ms")          # → 651
trial.get("accuracy")       # → None   (no error)
trial.get("accuracy", 0)    # → 0      (your own default)

#%% The dictionary toolbox
key_to_color = {"d": "red", "f": "green", "j": "blue", "k": "yellow"}

key_to_color["f"]               # → 'green'
"k" in key_to_color             # → True
key_to_color.get("x", "none")   # → 'none'
len(key_to_color)               # → 4
list(key_to_color.keys())       # → ['d', 'f', 'j', 'k']
list(key_to_color.values())     # → ['red', 'green', 'blue', 'yellow']
list(key_to_color.items())      # → [('d', 'red'), ('f', 'green'), ('j', 'blue'), ('k', 'yellow')]

key_to_color["x"] = "white"     # add
del key_to_color["x"]           # remove
len(key_to_color)               # → 4

#%% Looping over a dictionary
key_to_color = {"d": "red", "f": "green", "j": "blue", "k": "yellow"}

# A plain for loop gives you the keys
for key in key_to_color:
    print(key)
# → d
#   f
#   j
#   k

# .items() gives you key and value together - unpack them into two names
for key, color in key_to_color.items():
    print(f"{key}: {color}")
# → d: red
#   f: green
#   j: blue
#   k: yellow

#%% Counting with a dictionary
responses = ["blue", "yellow", "red", "red", "red"]

counts = {}
for response in responses:
    if response in counts:
        counts[response] += 1      # seen before: add one
    else:
        counts[response] = 1       # first time: start at one
print(counts)       # → {'blue': 1, 'yellow': 1, 'red': 3}

#%% Counting - the same thing with get()
counts = {}
for response in responses:
    counts[response] = counts.get(response, 0) + 1
print(counts)       # → {'blue': 1, 'yellow': 1, 'red': 3}

#%% Counting - trace it (one line per pass)
counts = {}
for response in responses:
    counts[response] = counts.get(response, 0) + 1
    print(response, counts)
# → blue {'blue': 1}
#   yellow {'blue': 1, 'yellow': 1}
#   red {'blue': 1, 'yellow': 1, 'red': 1}
#   red {'blue': 1, 'yellow': 1, 'red': 2}
#   red {'blue': 1, 'yellow': 1, 'red': 3}

#%% Start empty, or start at zero?
responses = ["blue", "yellow", "red", "red", "red"]

# Start empty: only what you saw appears
counts = {}
for response in responses:
    counts[response] = counts.get(response, 0) + 1
print(counts)       # → {'blue': 1, 'yellow': 1, 'red': 3}

# Start at zero: every category appears, even if it never happened
counts = {"red": 0, "green": 0, "blue": 0, "yellow": 0}
for response in responses:
    counts[response] += 1
print(counts)       # → {'red': 3, 'green': 0, 'blue': 1, 'yellow': 1}

#%% A trial as a record - a session as a list of records
len(session)                # → 18
session[2]                  # → {'trial': 3, 'word': 'GREEN', ... 'rt_ms': 651}
session[2]["rt_ms"]         # → 651
session[2]["word"]          # → 'GREEN'
session[-1]["trial"]        # → 18

#%% Looping over records
# Which trials were slower than 900 ms?
for trial in session:
    if trial["rt_ms"] > 900:
        print(trial["trial"], trial["condition"], trial["rt_ms"])
# → 7 neutral 922
#   9 incongruent 944
#   16 incongruent 904

#%% Looping over records - collect instead of print
slow = []
for trial in session:
    if trial["rt_ms"] > 900:
        slow.append(trial["trial"])
print(slow)                 # → [7, 9, 16]

#%% Grouping: a dictionary of lists
# Collect the reaction times of each ink color in its own list
rts_by_ink = {}
for trial in session:
    ink = trial["ink"]
    if ink not in rts_by_ink:
        rts_by_ink[ink] = []                  # first trial of this color
    rts_by_ink[ink].append(trial["rt_ms"])    # add to that color's list
print(rts_by_ink)
# → {'blue': [653, 712, 601, 636, 629], 'yellow': [657, 944, 904, 621],
#    'red': [651, 663, 622, 819, 710, 835], 'green': [612, 922, 695]}

#%% Grouping - the error: appending to a list that does not exist yet
rts_by_ink = {}
for trial in session:
    rts_by_ink[trial["ink"]].append(trial["rt_ms"])
# → KeyError: 'blue'

#%% Summarizing the groups
rts_by_ink = {}
for trial in session:
    ink = trial["ink"]
    if ink not in rts_by_ink:
        rts_by_ink[ink] = []
    rts_by_ink[ink].append(trial["rt_ms"])

for ink, rts in rts_by_ink.items():
    mean_rt = sum(rts) / len(rts)
    print(f"{ink}: {mean_rt:.1f} ms (n = {len(rts)})")
# → blue: 646.2 ms (n = 5)
#   yellow: 781.5 ms (n = 4)
#   red: 716.7 ms (n = 6)
#   green: 743.0 ms (n = 3)

#%% Tuples - you have met one already
result = "neuron:axon:synapse".partition(":")
result              # → ('neuron', ':', 'axon:synapse')
type(result)        # → <class 'tuple'>

screen = (1920, 1080)
screen[0]           # → 1920
len(screen)         # → 2

#%% Tuples - one element needs a comma
one = ("red",)
type(one)           # → <class 'tuple'>
not_one = ("red")
type(not_one)       # → <class 'str'>  (just a string in brackets)

#%% Tuples cannot be changed
ink_rgb = {"red": (255, 0, 0), "green": (0, 128, 0),
           "blue": (0, 0, 255), "yellow": (255, 255, 0)}

ink_rgb["blue"]         # → (0, 0, 255)
ink_rgb["blue"][2]      # → 255

#%% Tuples cannot be changed - the error
red = ink_rgb["red"]
red[1] = 100
# → TypeError: 'tuple' object does not support item assignment

#%% Unpacking, and returning more than one value
before, sep, after = "neuron:axon:synapse".partition(":")
before              # → 'neuron'

r, g, b = ink_rgb["yellow"]
r                   # → 255

def mean_and_n(values):
    """Return the mean and the count."""
    return sum(values) / len(values), len(values)

summary = mean_and_n([651, 663, 622])
summary             # → (645.3333333333334, 3)
mean_rt, n = mean_and_n([651, 663, 622])
n                   # → 3

#%% Tuples as dictionary keys - lists cannot be keys
# key = (block, trial): one value per trial, found by two numbers at once
rt = {(1, 3): 651, (1, 4): 712}
rt[(1, 4)]                  # → 712

#%% Tuples as dictionary keys - the error
rt = {[1, 3]: 651}
# → TypeError: unhashable type: 'list'
# keys must be values that cannot change

#%% Practise now 1 - Predict
d = {"a": 1, "b": 2}
d["a"] = d["a"] + 10
d["c"] = 3
print(len(d), d["a"])       # → 3 11

#%% Practise now 2 - Find the bug and fix it
words = ["DOG", "RED", "DOG", "BLUE"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1   # fixed: counts[word] += 1 raised KeyError
print(counts)               # → {'DOG': 2, 'RED': 1, 'BLUE': 1}

#%% Practise now 3 - Write it yourself
ages = {"sub-01": 19, "sub-02": 23, "sub-03": 21}
for participant, age in ages.items():
    if age > 20:
        print(participant)
# → sub-02
#   sub-03

#%% Looking ahead (Period 5) - the same list of dictionaries is a table
# Optional: not part of this period. Needs pandas (installed with Anaconda).
import pandas as pd

table = pd.DataFrame(session)
print(table.head(4))
# →    trial   word     ink    condition response  correct  rt_ms
#   0      1    DOG    blue      neutral     blue        1    653
#   1      2  TABLE  yellow      neutral   yellow        1    657
#   2      3  GREEN     red  incongruent      red        1    651
#   3      4    RED    blue  incongruent      red        0    712
