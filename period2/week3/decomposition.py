
"""
Created on Wed Nov 25 08:57:26 2026
NOTE: I commented out all the print statements to make things a bit easier to see while writing the code. Feel free to uncomment to see what they do

@author: Sonia
"""
# where I import my libraries
import csv 
import os
import numpy as np 
import matplotlib.pyplot as plt

# print("data" in os.listdir()) # If this isnt 'True', make sure your code (this file) is in the same folder as the data (available on canvas under week 3 materials)

#%% WHERE I WRITE ALL MY FUNCTIONS
def load_arrays(filename):
    """Return rt, condition, block, correct and responded as NumPy arrays.""" 
    # read data from file with dictreader
    with open(filename) as f:
        trials = list(csv.DictReader(f)) # trials is a dict
        
    # initialise empty lists
    rt = []
    condition = []
    block = [] # the block means that the participant did many rounds of the stroop task, and each round gets a nr. each participant does 4 blocks
    correct = [] 
    responded = []
        
    # we want to populate the lists with the relevant data
    for trial in trials:
        condition.append(trial["condition"]) # append current condition to condition list
        block.append(int(trial["block"])) # block 
        correct.append(int(trial["correct"])) # whether trial is correct or not - as 1 (correct) and 0 (true)
        if trial["response"] == "none": # a miss: rt_ms is ""
            rt.append(0.0) # placeholder; the mask removes it 
            responded.append(False)
        else:
            rt.append(float(trial["rt_ms"])) 
            responded.append(True)
    # !! Return !! each of the 5 data structures as numpy arrays    
    return (np.array(rt), np.array(condition), np.array(block), np.array(correct), np.array(responded))

def cell_means(filename):
    """Mean RT of correct valid trials, per condition and block (12 values).""" 
    # you're told to write this function with the input "filename", so that means we need to use the previous function 
    rt, condition, block, correct, responded = load_arrays(filename) 
    use = responded & (rt >= 150) & (correct == 1) # we write the mask inside the function (otherwise it's not available to the function)
    # initialise empty list. You're told this will have 12 values. 1 mean per block, 4 blocks per condition, 3 conditions -> 12 means
    means = [] 
    # the loop doesn't only compute the mean for each of the 12 cases, but it also sorts the values we add to the numpy array
    # start looping over conditions, then you loop over the blocks with the 2nd loop
    # -> loop nr 1 we get the mean for each block (2nd for loop) for congruent,
    # -> loop nr 2 - mean for each block (2nd loop) for "neutral"
    # -> loop nr 3 - same for incongruent
    for cond in ["congruent", "neutral", "incongruent"]: # we use this instead of for cond in cond, for b in block, because we want to enforce the order [For advanced programming: [ In theory, hard coding like this is not the best practice ]]
        for b in (1, 2 ,3, 4):
            means.append(rt[use & (condition == cond) & (block == b)].mean()) 
    # return all the means as an array        
    return np.array(means)

#%% MAIN (where I call my functions)
#%% PART 0 & 1
# testing on one participant
rt, condition, block, correct, responded = load_arrays("data/sub-01_stroop.csv") 
# printing the shape of each array to see that the dimensions of the data check out
# print("checking the shape of each arrays to make sure we have the right data")
# print(rt.shape, condition.shape, responded.shape) # should all be: (288,)

# valid when response is not none (we made it 1 if is some value and 0 if it is empty)
valid = responded & (rt >= 150) 
use = valid & (correct == 1) # mark for use in the decomposition analysis when valid and corrext
# we want to get the mean for each condition
# print("printing the mean per each condition:")
for cond in ["congruent", "neutral", "incongruent"]:
    is_cond = condition == cond
    # print(cond, round(rt[use & is_cond].mean(), 1),round(correct[valid & is_cond].mean(), 3))

# checking that the means function works
cell_means_test = cell_means("data/sub-01_stroop.csv") # check in variable explorer

#%% PART 2
rows = [] # initialise list
for p in range(1, 41):
    # for each row, get the means using the functions you just made
    rows.append(cell_means(f"data/sub-{p:02}_stroop.csv")) 
# stack all the rows so you get a 40(participants) x 12(means) matrix (remember that A(m x n) means m rows, n columns)
M = np.stack(rows)

os.makedirs("results", exist_ok=True) 
np.save("results/stroop_matrix_40x12.npy", M)

cond_by_block = M.mean(axis=0).reshape(3, 4) # if you want to get the mean per each block

# Want INTERFERENCE = INCONGRUENT - NEUTRAL
# we know M has the means for c, c, c, c, n, n, n, n, i, i, i, i on each row
#(c - congruent, n-neutral, i-incongruent)
# remember MATRIX MULTIPLICATION FROM LINEAR ALGEBRA, here we want to get Mw = I (Ax=b, and here I is the interference, not the identity matrix)
# M is 40x12, we want I to have interference for each participant, so it will be 40x1, so w has to be 12x1 (a weight for each block trial)

# if we do this for only one participant (M[0] @ w = I )
# c1*w1 + c2*w2 + c3*w3 + c4*w4 + 
# n1*w5 + ... +
# i1*w9 + ... + i4*w12

# we want the average interference per participant, so we want (I1 + I2 + I3 + I4)/4
# which is i1 - n1 + i2 - n2 + i3 - n3 + i4 - n4
# if we rearrange a bit, we can start to see what we need for the weights 
# if we notice that there is no c1, c2, c3, c4 in the sum above, so we can rearrange like this:
# c1*0 + c2*0 + ...
# n1*(-1) + ... # in the sum we subtract each n from each i, so it's multiplied by -1
# i1*1 + ... # and finally, we add each incongruent mean rt, so we essentially multiply by +1

# I recommend you write the full operations (without the '...') if you don't fully get it yet

# this means we want to set our 

w_interference = np.array(
    [0, 0, 0, 0, # the congruent mean rts don't play a role in the interferrence
     -1, -1, -1, -1, # we subtract the neutral mean rts
     1, 1, 1, 1]) # we add the incongruent mean rts
# to get the total interferrence effect, we average the interferrence over the 4 blocks, so we need to divide by 4 somewhere
interference = M @ w_interference / 4

#%% PART 3, 4, 5
# SVD - the goal is to used svd to *reduce the dimensions of the data*. Our stroop tasks only has 12 dimensions rn (each mean), but in real life, brain-related data are huuuge (ex.fmri gives a value for each pixel in a a 3d image for each time point) 

# Centering data
Mc = M - M.mean(axis=0) # centering data (this is the almost the same as getting the z-scores). The mean is now 0 and each subject can be above or below the mean from -1 to 1.
U, S, Vt = np.linalg.svd(Mc, full_matrices=False) # just the numpy command for singular value decomposition (CHECK LINEAR ALGEBRA SLIDES ON SVD FROM WEEK 7 + lecture for programming this week)
scores = U * S
# check results 
# print(U.shape, S.shape, Vt.shape) # or check in Variable explorer, should be ((40, 12), (12,), (12, 12))

# How many components
# components are ordered (descending from most variation explained)
# you want the components to describe enough of the data to draw conclusions for, but not so much that you again have too many dimensions
var_explained = S**2 / np.sum(S**2) 
# plot the variance explained by each component
plt.figure()
# loop over 12 components (from 1 to 13-1 if you remember from Period 1) to see how much variance each component explains
# why 12? our data already has 12 dimensions, so when we reduce it, we usually want some number (much) lower than the data dimensions
plt.plot(range(1, 13), var_explained * 100, "o-") 
plt.xlabel("Component")
plt.ylabel("Variance explained (%)")
plt.show() # examine in Plots tab, and you can see that the 1st component explains almost the entire data

print("cummulative sum of component variance effect")
print(np.round(np.cumsum(var_explained) * 100, 1)) # if you print the cummulative sum of variance explained
# you should see that the first component explaines 82.3% of the data, comp1+comp2 - 88.2%, 1+2+3 - 90.9% etc.

# What does each component describe

labels = [c[0].upper() + str(b) for c in ["congruent", "neutral", "incongruent"]
          for b in [1, 2, 3, 4]] # C1 ... C4, N1 ... N4, I1 ... I4 plt.xticks(range(12), labels)

plt.figure()
plt.plot(range(12), Vt[0], "o-", label="component 1") 
plt.plot(range(12), Vt[1], "s-", label="component 2") 
plt.axhline(0, color="gray", linewidth=0.8)
plt.xticks(range(12), labels) 
plt.legend()
plt.show()
# EXPLANATION
# Component 1: all 12 weights are about +0.3. A high score means the participan was slower in every cell (so every condition, every trial, every block) 
# Component 2: negative for the congruent and neutral cells, positive for the incongruent cells. -> Component 2 discriminates Incongruent vs other conditions
# A high score in component 2 means participant was (extra) slow on incongruent trials compared with the others  (which corresponds with the interference effect)
# Signs are arbitrary, if you get the opposite, the meaning is the same with the sign flipped. (so high score on 2, means faster times for C+N vs I)

# Check this with correlation
print(f'component 1 x Mean RT/partic: {np.corrcoef(scores[:, 0], M.mean(axis=1))[0, 1]:.2f}')
# compare scores of component 1 (index 0) with the mean scores of each participant → 1.00 
print(f"component 2 x Interference effet: {np.corrcoef(scores[:, 1], interference)[0, 1]:.2f}") 
# compare scores of component 2 with the interference effect (computed just before) → 0.93

#%% PART 6
# we use SVD to decompose data into smaller dimensions, but we can use the components to reconstruct the original data
# because the components describe the variation in the data itself.
M_reconstructed = scores[:, :1] @ Vt[:1] + M.mean(axis=0)  # (40, 1) @ (1, 12) → (40, 12) np.abs(M - col_means).mean() # → 57.8
# we look at some data metrics to see what the differences are between M and M_reconstructed
mean_diff = np.abs(M - M_reconstructed).mean()
std_recon = (M_reconstructed @ w_interference).std()
std_M = (M @ w_interference).std()
print(f'mean difference between reconstructed and original: {mean_diff:.2f}, str original: {std_M:.2f}, std reconstructed: {std_recon:.2f}')

# Plots
plt.figure()
plt.imshow(M, aspect="auto")
plt.title("Original Data - RT per block")

plt.figure()
plt.title("Reconstructed Data - RT per block")
plt.imshow(M_reconstructed, aspect="auto")


#%% MORE ON SVD
'''
What you (in theory) already know from linear algebra
    - SVD is the diagonalization of A by using A@A_transposed and A_transposed@A (where @ is matrix multiplication, just like the python syntax)
        --> U@S@V_transposed
    - diagonalization gives us [some matrix with eigenvectors][diagonal matrix of eigenvalues][some matrix with eigenvectors]
    - a diagonal matrix has an orthonormal basis
    - eigenvalue/vector pairs are interesting vecause they only scale, they don't rotate
    - orthogonal projection, change of basis

Why do we use SVD in data analysis?
Option 1 - Dimensionality reduction:
real life brain data is huuuuuuge. Here we only have 12 variables (the mean rt for each cobdition for each block), but even so 
in order to plot each of our 40 participants, we would have to have an axis for each of the 12 variables, and 12 is a bit 
inconvenient for actually being able to plot the data. You could plot each pair of coordinates, but then you'd still have 
12! (factorial) possible permutations, so at least ~ 400.000.000 plots X_X it then becomes almost impossible to see relationships 
(correlations, clusters etc) within the data. Now think of gene expression data ~ 10k variables (1 nr of mRNA level for each gene),
 or fMRI (3 space coordinates and several hundred-thousand time steps). It becomes unrealistic and bothersome.

 Fortunately, when we diagonalize the data, the U and V give us eigenvectors that describe the direction of most variance in these datasets. 
 Because the eigenVALUES are sorted in descending order, so are the eigenVECTORS (or 'COMPONENTS') will be in the order of most variance explained 
 to least variance explained (while remaining orthogonal to each other). Now you can take your 40 data points and project (onto the orthogonal 
 basis/change of coordinates in this new orthogona basis) and plot them onto just 2-3- a few of these components. Essentially, you only look at those 
 components of the data that describe the most variance - the aspect of the data that varies the most from one datapoint to another. 
 
Remember that the directions are sorted, so the first component will explain more of the variance than the second component, which will explain
more than the third etc. This can be C1: ~85% (like in the example) C2 ~10%, C3~4% etc. Or it can be C1:30% C2:14% C3:1% etc (any values). You 
usually then do a check (like the first plot or the cummulative sum) to see roughly how many comopnents you want to keep in your analysis (here 
we keep 2). You can then further further analyze the scores (the coefficients of the projection onto each component) of each component, and see
how they change across your data points compared to your variables (the original 12 RT means). See more on how to interpret the plot in the cmments
above. You also can check the correlation of the scores of each componenent to each of your variables.

Option 2 - Clustering (not explored in this exercise)
When you move from a 12-dimenstiona (n-dimensional) space to a 2-3 dimensional space you might be able to spot correlations in the data OR clusters
(literally, clouds of points that group together on the plot)

Option 3 - Data Compression 
This is a lie, we're actually going to look at data RECONSTRUCTION first. So again, your components explain the direction of most variance AND the
projection coefficients, so we can re-build the original dataset by doing the reverse operation (so far we went from X - data to -> U@S@V_tr, now we 
do U@S@V_transposed -> data - but only for the first few relevant components we selected in Option 1). You can then check to see how similar this 
reconstruction is to the original data. 

This is useful, for instance, to compress images (reduce their resolution ~ kinda) for sharing via mail for ex.
(where you have a maximum size limit), and then unpack the original images to a reconstructd resolution - hence, data compression

 

https://www.youtube.com/watch?v=KQ76Q3Efyxc <-- some nice visualizations, tho they talk a bit more about the math of it all, every now and then the 
graphics show what I am trying to explain. Focus on the clouds of data and the directions of larges variance (most spread)
'''