# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:58:45 2026

@author: Sonia
"""

hbb = "ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAAC"

#%% Task A count bases

# initialise dictionary
hbb_count={"A":0,"C":0,"G":0,"T":0}

# populate dictionary (with string operations in this case)
for base in hbb_count:
    hbb_count[base] = hbb.count(base)

# calculate CG content
cg_content = (hbb_count["C"] + hbb_count["G"])/len(hbb)

print(f'the hbb gene contains {cg_content*100:.2f}% C and Gs')

#%% Task B Partner Strand

# complement dictionary
complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
# empty string
comp_strand = ''
# build complementary string using complement dict
for base in hbb:
    comp_strand += complement[base]
# reversing the strand
rev_comp = comp_strand[::-1]

print(hbb)
print(rev_comp)

#%% TaskC

new_gene = "ATGGTNCAT"
new_count = {}
for base in new_gene:
    new_count[base] = new_count.get(base, 0) + 1

print(new_count)

#%% bonus
sickle = hbb[:19] + "T" + hbb[20:]

codon_table = {"ATG": "M", "GTG": "V", "CAT": "H", "CTG": "L", "ACT": "T",
"CCT": "P", "GAG": "E", "AAG": "K", "TCT": "S", "GCC": "A",
"GTT": "V", "TGG": "W", "GGC": "G", "AAC": "N"}

def translate(seq):
    peptide_seq =''
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        peptide_seq += codon_table[codon]
    return peptide_seq

print(f'  hemoglobin peptide: {translate(hbb)}')
print(f'sickle-c hbb peptide: {translate(sickle)}')

