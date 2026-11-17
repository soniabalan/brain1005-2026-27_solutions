# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:20:39 2026

@author: Sonia
"""

def dot_product (v1, v2): 
    # initialise product
    product = 0
    
    # check vector lengths
    if len(v1) != len(v2):
        print("vectors have unequal lengths. cannot perform dot product")
        return None
    else:
        for i in range(len(v1)):
            #print(f"index i: {i}")
            product = product + v1[i]*v2[i]
                
    return product


def matrix_vector(A, v):
    # initialise product 
    product = []
    
    # check size
    if len(A[0]) != len(v):
        print("cannot perform operation")
        return
    else: 
        for i in range(len(A)):
            product.append(dot_product(A[i],v))
    
    return product

def matrix_multiply(A, B):
    # initialise product 
    
    n_row = len(B) # nr rows of B
    n_row_A = len(A) # nr rows of A
    n_col = len(B[0]) # nr cols of B

    # A = m x n, B = n x p, product = m x p
    product = [[0] * n_col for _ in range(n_row_A)]

    
    # check size
    if len(A[0]) != len(B):
        print("cannot perform operation")
        return
    else: 
        # transpose B
        B_transposed = [[0] * n_row for _ in range(n_col)]
        for i in range(n_row):
            for j in range(n_col):
                B_transposed[j][i] = B[i][j]
        
        for i in range(len(A)):
            for j in range(len(B_transposed)):
                product[i][j] = dot_product(A[i], B_transposed[j])

    return product
    
    

print(dot_product([1, 2, 3], [4, 5, 6]))
print(dot_product([0, 0], [7, 9]))
print(dot_product([1, 1], [1, 2, 3]))

A = [[1, 2, 3], [4, 5, 6]] 
v = [1, 0, -1]
print(matrix_vector(A, v))

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
AB = matrix_multiply(A, B)  
print(AB)
