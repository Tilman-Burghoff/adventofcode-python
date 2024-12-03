with open("input.txt") as f:
    data = list(map(int, f.read().split()))
A, B = sorted(data[::2]), sorted(data[1::2])

print("Part 1:", sum(map(lambda x,y: abs(x-y), A,B)))

print("Part 2:", sum([i*B.count(i) for i in A]))