with open("input.txt") as f:
    data = f.readlines()

def is_allowed(report):
    is_increasing = int(report[1]) > int(report[0])
    last_el = int(report[0])
    for el in report[1:]:
        el = int(el)    
        if not (el > last_el) == is_increasing:
            return False
        if abs(el-last_el) not in [1,2,3]:
            return False
        last_el = el
    return True


data = list(map(lambda x: x.split(), data))

print("Part 1:", sum(map(is_allowed, data)))

print("Part 2:", sum(map(lambda report: any([is_allowed(report[:i]+ report[i+1:]) for i in range(len(report))])), data))