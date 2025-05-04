#!/usr/bin/python

"""
sum solver:
given a number of unique integer summands n
and a sum
show all possible solutions
"""

import sys
from itertools import combinations

NUM_SUDOKU = 9
SUDOKU_SET = set(range(1, NUM_SUDOKU + 1))

class SumSolver():
    def __init__(self):
        self.solver = dict()  # {N: {sum: [options]}}

       # loop through all possible n
        for i in range(1, NUM_SUDOKU + 1):
            if i not in self.solver:
                self.solver[i] = dict()
            combs = list(combinations(SUDOKU_SET, i))
            for comb in combs:
                this_sum = sum(comb)
                if this_sum not in self.solver[i]:
                    self.solver[i][this_sum] = [comb]
                else:
                    self.solver[i][this_sum].append(comb)

    # give a list of tuples of all combinations
    def solve(self, n: int, group_sum):
        return self.solver[n][group_sum]

def main():
    # print startup
    print("you have now entered sudoku jones")
    print("q to quit")
    print()

    solver = SumSolver()
    print("solver ready")

    while True:
        print("n sum")
        user_in = input()
        if user_in == "q":
            exit(0)

        # strip on white space
        user_in = user_in.split()
        num_args = len(user_in)
        if num_args == 2:
            result = solver.solve(int(user_in[0]), int(user_in[1]))
            for res in result:
                print(res)
        else:
            print("try n sum,")
            print("or q to quit")

if __name__ == "__main__":
    main()