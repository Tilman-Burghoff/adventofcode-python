from collections import defaultdict
from functools import cmp_to_key

with open("input.txt") as f:
    rules, data = f.read().split("\n\n")

rules = rules.split("\n")
forbidden_before = defaultdict(set)
for rule in rules:
    first, second = rule.split("|")
    if not forbidden_before[second]:
        forbidden_before[first] = {second}
    else:
        forbidden_before[first].add(second)


def are_correct(pages):
    seen = set()
    for page in pages:
        if first_page := seen.intersection(forbidden_before[page]):
            return False
        seen.add(page)
    return True


sort_key = cmp_to_key(lambda a,b: 1 - 2*(f"{a}|{b}" in rules))

part1_sum = 0
part2_sum = 0
for line in data[:-1].split("\n"):
    pages = line.split(",")
    if are_correct(pages):
        part1_sum += int(pages[len(pages)//2])
    else:
        part2_sum += int(sorted(pages, key=sort_key)[len(pages)//2])
        

print("Part 1:",part1_sum)
print("Part 2:",part2_sum)