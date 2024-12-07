from operator import add, mul

def is_solvalble(terms, solution):
    partial_solution = {int(terms[0])}
    for term in terms[1:]:
        term = int(term)
        new_solution = set()
        while partial_solution:
            sol = partial_solution.pop()
            for op in (add, mul, lambda sol, term: int(f"{sol}{term}")):
                new_solution.add(op(sol, term))
        partial_solution = new_solution
    return solution in partial_solution


with open("input.txt") as f:
    output = 0
    for line in f.readlines():
        solution, terms = line.split(": ")
        solution = int(solution)
        if is_solvalble(terms.split(), solution):
            output += solution

print(output)