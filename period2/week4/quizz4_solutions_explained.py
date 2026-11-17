"""
This is the solution for test version B. You can apply the same reasoning for version A, only some 
values are different, but the code is basically the same. DO NOT MAKE NEW LINES, I refer to specific line numbers here and there

THE COMMENTS ARE MORE IMPORTANT THAN THE "right answer" 
"""
#%% Section 1 - MCQ
# 1.  What does result contain after the last line has run?
print("1.  What does result contain after the last line has run? \n--------------")

def count_fast(rts):
    n = 0
    for rt in rts:
        if rt < 500:
            n += 1
    print(n)
 
result = count_fast([450, 620, 480])
'''Answer: None. There is no return statement, so the variables inside the function (n)
are NOT available outside of this function. Therefore, calling the function with some
values (i.e. line 16), will print the output 2, but 2 will not be saved and assigned to
[result]'''

# 2.  Which expression is True?
print("2.  Which expression is True? \n--------------")
trial = {"word": "GREEN", "ink": "red", "correct": 0}
print(f'A) {"correct" in trial}') # correct, because "in [dictionary]" looks at the key names and "correct" is a key in the dictionary
print(f'B) {"red" in trial}') # not correct because "in [dictionary]" doesn't care about values, and "red" is a value of the key "ink"
# C will give an error, so I commented it out
# print(f'C) {trial[2] == 0}') # dictionaries are indexable by name (of the keys), but not by number
print(f'D) {trial.get("rt_ms") == 0}') # the .get() method extracts the value for a given key,but there is no key for "rt_ms". 
# This would be true for trial.get("rt_ms",0) == 0, because the second parameter (in this case, "0") will create a "rt_ms" key, with a default value of 0


# 3.  Which line raises an error?
print("3. Which line raises an error? \n--------------")
positions = {"fixation": (0, 0), "target": (200, 150)} 
''' Check the variable explorer for this ex '''
x, y = positions["target"] #A) no error. x = 200 float, y = 150 float (or int) 
positions["cue"] = (-200, 150) # B) no error, will add "cue":(-200, 150) to the dict
print(positions["target"][0]) # C) no error, will print 200 (which is the 0th value of the "target" tuple)
# positions["target"][0] = 250 # D) ✓ correct. 
'''The error is because positions["target"] is a tuple, and the operations (=, as opposed to ==)
tries to change the 0th element in the tuple, however tuples are not changeable'''

# 4. This row was read from a CSV file with csv.DictReader. Which expression is True for this slow trial (reaction time above 800 ms)?
print("4. This row was read from a CSV file with csv.DictReader. Which expression is True for this slow trial (reaction time above 800 ms)? \n--------------")
row = {"trial": "9", "correct": "1", "rt_ms": "845"}
float(row["rt_ms"]) > 800 
'''✓ correct because the value of "rt_ms" is a string, so the comparison only works when 
converting to a float. for the same reason, the other answers were wrong. the "csv.DictReader" part is a red herring'''
# # other answer options:
# row["rt_ms"] > 800
# row["rt_ms"] == 845
# row["rt_ms"] > "900"

#%% Section 2 - Read the code

# 5. Read the code below. Fill in the table with the values of cond, n_errors and rts at the end of each pass through the loop.
print("5.  Read the code below. Fill in the table with the values of cond, n_errors and rts at the end of each pass through the loop. \n--------------")
'''the table is asking you for the values for: cond, n_errors, and rts. 
I will just add a line to print these 3 out at the end of each loop, and add a counter for the print to be nice'''

pass_nr = 1 # I added this line, not in the test
session = [
    {"condition": "congruent", "correct": 1, "rt_ms": 610},
    {"condition": "congruent", "correct": 0, "rt_ms": 580},
    {"condition": "neutral", "correct": 1, "rt_ms": 640},
    {"condition": "congruent", "correct": 1, "rt_ms": 630},
]
 
rts = {} # here we can note that rts is a dictionary
n_errors = 0 # n_errors starts as 0 outside of the loop
for trial in session:
    cond = trial["condition"] # every loop, cond becomes a string corresponfing to the value of the "condition" key of the trial dictionary
    if trial["correct"] == 1:
        if cond not in rts:
            rts[cond] = [] # rts[cond] is a list, and values are appended to each cond key (when correct = 1)
        rts[cond].append(trial["rt_ms"])
    else:
        n_errors += 1 # when correct is not ==1, n_errors increases by 1 (IT DOES NOT RESET TO 0)
    # I added the next 2 lines, not in the test    
    print(f'pass {pass_nr}:  cond: {cond}, n_errors: {n_errors}, rts: {rts}')
    pass_nr += 1

# 6. What do the three print lines show?
print("6. What do the three print lines show? \n--------------")

def label(acc, minimum=0.8):
    if acc >= minimum:
        result = "include"
    else:
        result = "exclude"
    return result
 
print(label(0.75)) # acc takes on the value 0.75, minimum takes the default value of 0.8
print(label(0.75, 0.7)) # the first value gets associated with the first parameter, so acc = 0.75, 
# the 2nd value overwrites the 2nd parameter default value, so minimum = 0.7
print(label(minimum=0.9, acc=0.85)) # the order of the parameters is ignored, so the parameters 
# take values as indicated in the function call, so acc = 0.85, minimum= 0.9

#%% Section 3 - Find and Fix

# 7. This program should print the improvement in accuracy from block 1 to block 2, 0.25. Instead, it prints two numbers and then stops with an error.
print("7. This program should print the improvement in accuracy from block 1 to block 2, 0.25. Instead, it prints two numbers and then stops with an error. \n--------------")

'''
def accuracy(correct):
    acc = sum(correct) / len(correct)
    print(acc)
 
block1 = accuracy([1, 1, 0, 1])
block2 = accuracy([1, 1, 1, 1])
improvement = block2 - block1
print(improvement)
'''
''' 
A) describe the error: 
    there is no return in the function definition, so block1 and block 2 will not get any value 
    assigned to them. You then cannot make operations with empty variables
B) fix the line (110)
'''

def accuracy(correct):
    acc = sum(correct) / len(correct)
    return(acc) # Fixed line
 
block1 = accuracy([1, 1, 0, 1])
block2 = accuracy([1, 1, 1, 1])
improvement = block2 - block1
print(improvement)


# 8. This code builds the partner strand of a DNA sequence. The sequencer could not read one base and wrote "N". The program should store "N" for any base that is not in the table and print ['C', 'N', 'T', 'G'], but it stops with an error.
print("8.This code builds the partner strand of a DNA sequence. The sequencer could not read one base and wrote \"N\". The program should store \"N\" for any base that is not in the table and print [\'C\', \'N\', \'T\', \'G\'], but it stops with an error.  \n--------------")

'''
partner = {"A": "T", "T": "A", "C": "G", "G": "C"}
bases = ["G", "N", "A", "C"]
complement = []
for base in bases:
    complement.append(partner[base])
print(complement)
'''
'''
A) Which error does Python raise, and on which base? 
    KeyError: 'N', on the second base ("N")
    I also accepted a description that mentioned that "N" is not one of the existing keys in the partner dictionary
    (keywords: "key") <-- ironic, i know
B) Rewrite the line (142) inside the loop so that the program prints the expected output
Note, several of you changed the dictionary instead of fixing the loop. Read the instructions carefully
'''

partner = {"A": "T", "T": "A", "C": "G", "G": "C"}
bases = ["G", "N", "A", "C"]
complement = []
for base in bases:
    complement.append(partner.get(base,"N")) 
    # the first argument in get (base) will find the corresponding base as present in the dictionary
    # the 2nd argument is the default. so if it cannot find current base in the keys of the dict, it will return the value "N"
print(complement)

# Alterbative
partner = {"A": "T", "T": "A", "C": "G", "G": "C"}
bases = ["G", "N", "A", "C"]
complement = []
for base in bases:
    if base in partner:
        complement.append(partner[base])
    else:
        complement.append("N")
print(complement , "alternative solution")


#%% Section 4 - Write your onw 
# there are several ways to solve these, so if you thought of an alternative solution, you got the points

# 9. Write a function is_error(trial) that takes one trial dictionary and returns True when the response does not match the ink color, and False otherwise.
print("9. Write a function is_error(trial) that takes one trial dictionary and returns True when the response does not match the ink color, and False otherwise. \n--------------")
'''
is_error({"word": "BLUE", "ink": "yellow", "response": "blue"})   → True
is_error({"word": "BOX", "ink": "red", "response": "red"})        → False
'''

def is_error(trial): # if it has 'def' it's a functino definition. the definition is for every possible parameter value (variable in def - parameter)
    return trial["response"] != trial["ink"]
# NOTE a lot of you did return is_error["ink"] == is_error["response"]. 
# is_error is the name of the function, the dictionary you want to access the values from is trial
print(is_error({"word": "BLUE", "ink": "yellow", "response": "blue"})) # a function is called after it's defined. 
# the function call is a particular instance, that works for the exact value passed as the argument (variable in call - argument)
# here, it's called inside the print function, with the value {"word": "BLUE", "ink": "yellow", "response": "blue"} - a dictionary
print(is_error({"word": "BOX", "ink": "red", "response": "red"}) )

# 10.  
print("10. Write a function correct_counts(session) that takes a list of trial dictionaries, like the one in Question 5, and returns a dictionary with the number of correct trials (trials where \"correct\" is 1) in each condition. All three conditions must appear, even when a condition has no correct trials. \n--------------")

'''
Let's break down the elements in the instructions
Write a 
- function correct_counts(session) that
    --> shoudl have 'def function_name(parameters)' and we're given the function name and parameters, so we can start with: 
    def correct_counts(session): 
- takes a list of trial dictionaries, like the one in Question 5, 
    --> we know to expect sessions (the parameter) to be a list with a dictionary as each element 
    this suggests a for loop might be needed
- returns a dictionary 
    --> always always have a return statement, not (just) a print
    here we need to remember to retun as a dictionary, let's call it counts
- with the number of correct trials (trials where "correct" is 1) in each condition.
    --> we need to check if the trial is correct
        if trial["correct"] == 1:
    --> counts needs to have the keys as each condition, and the values as the nr of correct trials in that conditiont
    our conditions are "congrient", "neutral" and "incongruent". we don't know the values for each key, 
    as it depends on the arguments we pass in the function, so I'll just write "nr condition" and remember we want an int for each of those
    at the end, counts should be something like: {"correct" : nr correct, "neutral" : nr neutral, "incongruent" : nr incongruent } 
    --> to count, you usually have to 
        - instantiate (begin) with variables at 0 - we have a few options here, more instructions later give a bit more of an indication
            option A: counts = {} -- just an empty dict (increase count with the .get() method)
            option B: n_condition (for each condition) = 0, and at the end just put it all up in a dictionary
                n_congruent = 0, n_neutral = ), n_incongruent = 0
            option C: counts = {"correct" : 0, "neutral" : 0, "incongruent" : 0 }
        - and increas += 1 everytime a condition is met.
            option A: counts[conddition] = counts.get(condition, 0) + 1 # will add a condition every time it encounters a new one, and start that with 0 as the default, then we add 1
            option B: 
                if condition == "congruent":
                    n_congruent += 1 
                # and then the same for neutral and incongruent
            option C: counts[condition] += 1
- All three conditions must appear, even when a condition has no correct trials.
    --> this indicates we want to go with option C (or B), such that it shows 0 when no trials are correct in any given condition


AFTER I've considered all of these things, I put it all together (I will use option C, not B)
'''
# Answer
def correct_counts(session):
    counts = {"congruent": 0, "neutral": 0, "incongruent": 0}
    for trial in session:
        if trial["correct"] == 1:
            counts[trial["condition"]] += 1
    return counts
# Testing it out 
session = [
    {"condition": "congruent", "correct": 1, "rt_ms": 610},
    {"condition": "congruent", "correct": 0, "rt_ms": 580},
    {"condition": "neutral", "correct": 1, "rt_ms": 640},
    {"condition": "congruent", "correct": 1, "rt_ms": 630},
] # same as in Ex. 5

print(correct_counts(session)) 
# we expect correct_counts(session)  → {"congruent": 2, "neutral": 1, "incongruent": 0}
