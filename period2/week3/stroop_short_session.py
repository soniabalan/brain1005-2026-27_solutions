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
