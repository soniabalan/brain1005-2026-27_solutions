# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:49:04 2026

@author: Sonia
"""

def is_congruent(word, ink_colour):
    return word.lower() == ink_colour.lower()

print(is_congruent("RED", "red"))
print(is_congruent("RED", "blue"))
print(is_congruent("DOG", "blue"))