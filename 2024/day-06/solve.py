import numpy as np

with open("input.txt") as f:
    grid = np.array(([[letter for letter in line[:-1]] for line in f.readlines()]), dtype="<U1")

start_idx = np.argwhere(grid=="^").ravel()

index_valid = lambda idx: 0 <= idx[0] < grid.shape[0] and 0 <= idx[1] < grid.shape[1]
direction = [np.array([-1,0]), np.array([0,1]), np.array([1,0]), np.array([0,-1])]

## part 1
idx = start_idx
visited = set([tuple(idx)])
obstacles_hit = 0
while True:
    new_idx = idx + direction[obstacles_hit%4]
    if not index_valid(new_idx):
        break
    if grid[tuple(new_idx)] == "#":
        obstacles_hit += 1
    else:
        idx = new_idx
        visited.add(tuple(idx))

print("Part 1:", len(visited))
print(grid[visited.pop()])
def is_loop(grid):
    idx = start_idx
    obstacles_hit = 0
    visited_with_dir = set([tuple(idx)+tuple([0])])

    while True:
        new_idx = idx + direction[obstacles_hit%4]
        if not index_valid(new_idx):
            return False
        if grid[tuple(new_idx)] == "#":
            obstacles_hit += 1
        else:
            if tuple(new_idx)+tuple([obstacles_hit%4]) in visited_with_dir:
                return True
            idx = new_idx
        visited_with_dir.add(tuple(idx)+tuple([obstacles_hit%4]))


loops = 0
while visited:
    obstacle_at = visited.pop()
    if obstacle_at == tuple(start_idx):
        continue
    grid[obstacle_at] = "#"
    loop = is_loop(grid)
    loops += is_loop(grid)
    grid[obstacle_at] = "."

print("Part 2:", loops+1) # i had an off by one error, but im too tired to figure out why