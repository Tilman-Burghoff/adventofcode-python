import numpy as np
with open("input.txt") as f:
    data = np.array(([list(map(int, x[:-1])) for x in f.readlines()]))

def compute_view_dist(slice):
    if len(slice) == 1:
        return 0
    is_blocking = slice[1:]>=slice[0]
    return np.argmax(is_blocking) + 1 if np.any(is_blocking) else len(is_blocking)


def compute_scores(arr):
    scores = np.zeros_like(arr)
    for t in range(arr.size):
        row, col = (t//arr.shape[0], t%arr.shape[1])
        score = compute_view_dist(arr[row, col:].ravel())
        score *= compute_view_dist(arr[row, :col+1].ravel()[::-1])
        score *= compute_view_dist(arr[row:, col].ravel())
        score *= compute_view_dist(arr[:row+1, col].ravel()[::-1])
        scores[row, col] = score
    return scores

result = compute_scores(data)

print(np.max(result))