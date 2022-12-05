import aoc_utils

input_string = aoc_utils.getInputString(4)
input_list = input_string.strip().split()
pairs = [n.split(",") for n in input_list]

def getRange(elf):
    section = [int(n) for n in elf.split("-")]
    return section

def isContained(section_a, section_b):
    a, b = section_a
    x, y = section_b
    range1 = range(a, b+1) # Inclusive last number
    range2 = range(x, y+1)
    p1_p2_tuple = (
        (range1.start in range2 and range1.stop -1 in range2) or 
        (range2.start in range1 and range2.stop -1 in range1),
        (range1.start in range2 or range1.stop -1 in range2) or
        (range2.start in range1 or range2.stop -1 in range1)
    )
    return p1_p2_tuple 

def checkWork(pair):
    elf_a, elf_b = pair
    elf_a_range = getRange(elf_a)
    elf_b_range = getRange(elf_b)
    return isContained(elf_a_range, elf_b_range)

def part_one():
    count = 0
    for pair in pairs:
        count += checkWork(pair)[0]
    print(count)

def part_two():
    count = 0
    for pair in pairs:
        count += checkWork(pair)[1]
    print(count)

part_one()
part_two()