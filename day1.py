"""
Day 1:
Calorie Counting
"""

from operator import itemgetter

elves = []
elf = []
with open("input/day1.txt") as f:
    for line in f:
        l = line.rstrip()
        if not l:
            elves.append((sum(elf), elf.copy()))
            elf.clear()
        else:
            elf.append(int(l))

descending_elves = sorted(elves, key=itemgetter(0), reverse=True)
# Problem 1
print(descending_elves[0][0])

# Problem 2, top three
print(sum([n[0] for n in descending_elves[:3]]))

