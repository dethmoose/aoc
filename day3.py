import aoc_utils
import string

input_string = aoc_utils.getInputString(3)
# List for part one
input_list = input_string.strip().split() 
# Grouped list for part two
groups = [input_list[i:i+3] for i in range(0, len(input_list), 3)]

def getCommonItemType(comp_a, comp_b):
    for letter in comp_a:
        if letter in comp_b:
            return letter

def sumPriority(common_item):
    if common_item.islower():
        for i, letter in enumerate(string.ascii_lowercase):
            if letter == common_item:
                return i + 1
    else:
        for i, letter in enumerate(string.ascii_uppercase):
            if letter == common_item:
                return i + 27

def getBadge(group):
    a,b,c = [set(n) for n in group]
    common = a.intersection(b,c)
    return list(common)[0]

def part_one():
    priority_sum = 0
    for rucksack in input_list:
        compartment_a = slice(0, len(rucksack) // 2)
        compartment_b = slice(len(rucksack) // 2, len(rucksack))
        common_item = getCommonItemType(rucksack[compartment_a], rucksack[compartment_b])
        priority_sum += sumPriority(common_item)
    print(priority_sum)

def part_two():
    priority_sum = 0
    for group in groups:
        badge = getBadge(group)
        priority_sum += sumPriority(badge)
    print(priority_sum)

part_one()
part_two()