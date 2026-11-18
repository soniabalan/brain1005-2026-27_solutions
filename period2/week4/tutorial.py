"""
Tutorial 4 Period 2 November 18th 
Plotting in Python

Created on Tue Nov 17 17:16:08 2026
"""
#%% Part 0 - SETUP

# to plot in python you need to use libraries. Essentially, Python is too dumb and can't do plots, so you 
# need to borrow some pre-made functions from somewhere else. In this case, it's a public library called 
# matplot lib. 
import matplotlib.pyplot as plt
from load_csv import load_csv # load_csv lets us use custom pre-made functions, that were made by the course
# coordinators. we still borrow these function from somewhere else, but this time, it's another file in the
# SAME FOLDER.

conditions, mean_rts, sd_rts, interference, facilitation, positive = load_csv() # we call the load_csv() function
# CHECK: compare with the return statement of load_csv() and make sure all the variables are the same 
#   they should be in the same order, the names can be different (ex. the code will work for: 
# condts, MeanRts, SDRts, interf, fac, pos = load_csv()     
# it will just assign the value of mean_rts (from inside the function) to the variable called MeanRts here.
# Look at the Variable Explorer before moving on!!

# printing some of the info to check everything worked fine
print(f"Loaded {len(interference)} participants")
print("Mean RTs (ms):", [round(rt, 1) for rt in mean_rts])

#%% Part 1 - COMPARE REACTION TIMES (+5 REFINE, INTERPRET, SHARE)
# Change the view on the right from Variable Explorer to Plots.
plt.figure()
plt.bar(conditions, mean_rts, color = ['#583252', '#feb23f', '#cd1453'],# added colour argument
        yerr=sd_rts, capsize=4) # from part 5
# if you want pretty colours you can look up colour palettes on the internet and search for "hex codes"
plt.title("Mean reaction time by Stroop condition +- 1SD")
plt.xlabel("Stroop condition")
plt.ylabel("Mean reaction time (ms)")
# always start your barplots in 0
plt.ylim(0, 850) # the other option shows you how data manipulation works (like on the news and such)
plt.grid(axis="y", alpha=0.25) # added gridlines from instructions
plt.tight_layout()
plt.show()

# bar plots are useful for showing quantities, when your data is stored in discrete categories (here: conditions)
# I personally hate them. Tables are usually just as informative and more space efficient
# Box plots >>>> Bar plots (they show you more meaningful information than a bar)
#%% Part2 - VARIATION AND RELATIONSHIPS
plt.figure()
# histograms plot discrete data. to make our continuous data (interference can take any value) discreete, we bin it (group it)
plt.hist(interference, bins = 18, color = '#583252') 
plt.title("Interference per participants") # remember to change title and axis labels
plt.xlabel("Interference effect (ms)")
plt.ylabel("Nr of participants")
plt.ylim(0, 20) # if you want to not hassle with finding meaningful ylims, you can normalise your data (divide everything by the mean), and then this axis is from 0-1. The hist will then show proportions of data per bin
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.show()

# histograms are useful to show data distributions (can check for normality, find peaks), usually used in data exploratory step
#%% Part 3 - DO EFFECTS VARY TOGETHER?
plt.figure()
plt.scatter( # can also use this syntax for plots when you have a lot of arguments and don't want all of them in one line
    x = interference,
    y = facilitation,
    color = '#583252',
    alpha = 0.75, # alpha is a transparency parameter. here it's 75% opaque. Helps you see clusters of data a bit easier
    label="Participants") # from part 5
plt.title("Interference vs. Facilitation")
plt.xlabel("Interference (ms)")
plt.ylabel("Facilitation (ms)")
plt.axvline(0, color="gray", linestyle="--", label="Zero interference") # from part 5
plt.xlim(min(interference)-5, max(interference)+5) # another trick to not really have to trial and error axis limits
plt.ylim(min(facilitation)-5, max(facilitation)+5) 
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.legend(loc='upper right') #from part 5
plt.show()

# scatter plots are very good at showing corelations, as well as data distribution (along 2 variables) and clustering
#%% Part 4 - LINEPLOT
ranked = sorted(interference)
ranks = range(1, len(ranked) + 1)

# Start a new figure and plot ranks against ranked.
# Label the axes, include ms, then show the figure.
fig, ax = plt.subplots()
ax.plot(ranks, ranked,
         marker = 'x',
         markersize = 5,
         linestyle='none')
ax.set_title("Ranked Interference")
ax.set_xlabel("Rank (participants)")
ax.set_ylabel("Facilitation (ms)")
ax.set_xlim(0, max(ranks))
ax.set_ylim(min(interference), max(interference)) 
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
plt.show()

# line plots are usual when you have some ordered data (here it's rank, time-series data is also a common one, ROC curves etc.)
#%% BONUS
# If you want to look more into what makes a good plot (in general), I can recommend:
# https://www.youtube.com/watch?v=BwtwOqdlY5E
# https://visme.co/blog/color-blind-friendly-palette/