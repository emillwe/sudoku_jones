#!/usr/bin/python

from itertools import combinations
import sys

if len(sys.argv) != 3:
    print("Usage: python sudoku_help.py <N> <sum>")

# Sudoku helper
NUM_SUDOKU = 9

def get_options(n, group_sum):
    sudoku_set = set(range(1, NUM_SUDOKU + 1))

    # dict: N -> dict: sum -> list
    solver_dict = dict() # {N: {sum: [options]}}
    for i in range(1, NUM_SUDOKU + 1):
        if i not in solver_dict:
            solver_dict[i] = dict()
        # get all combinations of n=1 (e.g. n=9 gives [1, 2, 3, 4, 5, 6, 7, 8, 9])
        combs = list(combinations(sudoku_set, i))
        for comb in combs:
            this_sum = sum(comb)
            if this_sum not in solver_dict[i]:
                solver_dict[i][this_sum] = [comb]
            else:
                solver_dict[i][this_sum].append(comb)

    return solver_dict[n][group_sum]

result = get_options(int(sys.argv[1]), int(sys.argv[2]))

for tup in result:
    print(tup)