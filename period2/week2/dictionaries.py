# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:15:56 2026

@author: Sonia
"""

#%% Part 3 Formulat to concentration     
atomic_mass = {
    "H": 1.008, "C": 12.011, "N": 14.007, 
    "O": 15.999, "Na": 22.990, "Cl": 35.45, 
    "K": 39.098, "Ca": 40.078
    }

#%% TASK A
# make a formulat that computes molar mass from formula
def molar_mass(formula):
    '''
    takes a dictionary as an input that has "atom": nr atoms as each entry
    computes the molar mass of the compound using the atomic_mass dictionary(table)
    '''
    # initialise mass
    mass = 0
    # loop over formula elements
    for element, nr_atoms in formula.items():
        # add mass of each element * nr atoms
        mass+= nr_atoms*atomic_mass[element]
    # return final mass    
    return round(mass,2)



#%% TASK B
# create lookup table
formulas = {
    "glucose" : {"C":6, "H":12, "O":6},
    "NaCl" : {"Na":1, "Cl":1},
    "KCl": {"K":1, "Cl":1},
    "CaCl2" : {"Ca":1, "Cl":2},
    "urea" : {"C":1, "H":4, "N":2, "O":1}
    }

mass_table = {}
for compound, formula in formulas.items():
    mass_table[compound] = molar_mass(formula)
    
print(f'{mass_table} g/mol') 

#%% TASK C
# returns concentration based on mass in table
def concentration(compound, mass_g, volume_l):
    '''
    parameters: which compound (from the mass_table), mass (in grams), volume (in L)
    returns concentration (mmol/L)
    '''
    mass_mol = mass_table[compound]
    mmol = (mass_g/mass_mol)*1000
    
    return round(mmol/volume_l, 2)
    
print(f'NaCl molar concentration: {concentration("NaCl", 9.0, 1)} (mmol/L')
print(f'glucose molar concentration: {concentration("glucose", 50, 1)} (mmol/L)')

#%% bonus
def grams_needed(compound, concentration_mol_l, volume_l):
    n_mol = concentration_mol_l * volume_l
    return round(mass_table[compound]*n_mol, 2)

print(f'we need: {grams_needed("KCl", 150/1000, 250/1000)} (mmol/L)')


