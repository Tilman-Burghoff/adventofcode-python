import numpy as np
import itertools

with open("input.txt") as f:
    data = np.array(([[letter for letter in line[:-1]] for line in f.readlines()]), dtype="<U1")

def is_XMAS(data, mask, row, col):
    rows = row + mask[0]
    cols = col + mask[1]
    if np.any(rows < 0) or np.any(rows >= data.shape[0]):
        return 0
    if np.any(cols < 0) or np.any(cols >= data.shape[1]):
        return 0
    return "".join(data[rows, cols]) == "XMAS"

def is_X_MAS(data, row, col):
    if row == 0 or row == data.shape[0]-1:
        return False
    if col == 0 or col == data.shape[1]-1:
        return False
    if {data[row-1, col-1], data[row+1, col+1]} != {"M","S"}:
        return False
    if {data[row+1, col-1], data[row-1, col+1]} != {"M","S"}:
        return False
    return True

directions = list(itertools.product((0,-1,1), (0,-1,1)))
input_masks = [(np.arange(4)*d[0], np.arange(4)*d[1]) for d in directions[1:]]

count_XMAS = 0
count_X_MAS = 0

for t in range(data.size):
    row, col = (t//data.shape[0], t%data.shape[1])
    if data[row, col] == "X":
        for mask in input_masks:
            count_XMAS += is_XMAS(data, mask, row, col)
    elif data[row, col] == "A":
        count_X_MAS += is_X_MAS(data, row, col)

print("PArt 1:", count_XMAS)
print("Part 2:", count_X_MAS)