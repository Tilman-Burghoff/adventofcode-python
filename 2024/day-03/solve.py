import re

with open("input.txt") as f:
    data = f.read()

def eval_match(match):
    return int(match[1]) * int(match[2])

pattern = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")

commands = pattern.findall(data)

active = True
result1 = 0
result2 = 0
for command in commands:
    if command[0] == "do()":
        active = True
    elif command[0] == "don't()":
        active = False
    else:
        result1 += eval_match
        if active:
            result2 += eval_match(command)

print("Part 1:", result1)
print("Part 2:", result2)