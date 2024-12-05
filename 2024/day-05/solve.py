from collections import defaultdict

with open("input.txt") as f:
    rules, data = f.read().split("\n\n")

forbidden_before = defaultdict(set)
for rule in rules.split("\n"):
    first, second = rule.split("|")
    if not forbidden_before[second]:
        forbidden_before[first] = {second}
    else:
        forbidden_before[first].add(second)


def pages_wrong(pages):
    seen = set()
    for page in pages:
        if first_page := seen.intersection(forbidden_before[page]):
            return (first_page.pop(), page)
        seen.add(page)
    return ()


def order_pages(pages, wrong_pair):
    while wrong_pair:
        i = pages.index(wrong_pair[0])
        j = pages.index(wrong_pair[1])
        pages[i], pages[j] = pages[j], pages[i]
        wrong_pair = pages_wrong(pages)
    return pages


part1_sum = 0
part2_sum = 0
for line in data[:-1].split("\n"):
    pages = line.split(",")
    if wrong_pair := pages_wrong(pages):
        part2_sum += int(order_pages(pages, wrong_pair)[len(pages)//2])
    else:
        part1_sum += int(pages[len(pages)//2])

print("Part 1:",part1_sum)
print("Part 2:",part2_sum)