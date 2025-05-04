#!/usr/bin/python

"""
sum solver:
given a number of unique integer summands n
and a sum
show all possible solutions
"""

import sys
from itertools import combinations
from logging import lastResort

NUM_SUDOKU = 9
SUDOKU_SET = set(range(1, NUM_SUDOKU + 1))

class SumSolver():
    def __init__(self):
        self.last_solution = list()
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
        self.last_solution = self.solver[n][group_sum]
        return self.last_solution

    def filter_solution(self, to_remove: int):
        if not self.last_solution:
           print("no solutions yet: please solve before filtering")
        for sol in self.last_solution:
            if to_remove in sol:
                self.last_solution.remove(sol)

def main():
    # print startup
    print("you have now entered sudoku jones")
    print("q to quit")
    print()

    solver = SumSolver()
    print("solver ready")
    # TODO: refactor -- func to handle user input
    while True:
        print("n sum")
        user_in = input()
        if user_in == "q":
            exit(0)

        # strip on white space
        user_in = user_in.split()
        num_args = len(user_in)
        if num_args == 2:
            if user_in[0] == 'r':
                solver.filter_solution(int(user_in[1]))
            else:
                solver.solve(int(user_in[0]), int(user_in[1]))
            for sol in solver.last_solution:
                print(sol)
        else:
            print("try n sum,")
            print("or q to quit")

if __name__ == "__main__":
    main()