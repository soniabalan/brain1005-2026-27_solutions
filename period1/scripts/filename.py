"""
Tutorial 16. September
"""

part1 = 601
part2 = 578
part3 = 592


# average over all RTs
average = (part1+part2+part3)/3/1000

## alternative: 
reaction_times = {part1/1000, part2/1000, part3/1000}
average2 = sum(reaction_times)/len(reaction_times)

# round the average
average_rounded = round(average2, 3)

# 
if average_rounded <= 0.6:
    print("faster than average")

print(average_rounded)









