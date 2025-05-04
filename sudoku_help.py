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
        self.solver = dict()  # {N: {sum: [options]}}
        self.prev_solution = list()
        self.commons = set()

       # loop through all possible n
        for i in range(1, NUM_SUDOKU + 1):
            if i not in self.solver:
                self.solver[i] = dict()
            combs = set(combinations(SUDOKU_SET, i))
            for comb in combs:
                this_sum = sum(comb)
                if this_sum not in self.solver[i]:
                    self.solver[i][this_sum] = [comb]
                else:
                    self.solver[i][this_sum].append(comb)

    # give a list of tuples of all combinations
    def solve(self, n: int, group_sum: int):
        self.prev_solution = self.solver[n][group_sum]
        return self.prev_solution

    # remove all options containing a given int
    def filter_solution(self, to_remove: int):
        if not self.prev_solution:
            print("no solutions yet: please solve before filtering")
            return list()
        for sol in self.prev_solution:
            if to_remove in sol:
                self.prev_solution.remove(sol)
        return self.prev_solution

    def winnow(self, to_remove: int):
        if not self.prev_solution:
            print("no solutions yet: please solve before filtering")
            return list()

        n = len(self.prev_solution[0])
        s = sum(self.prev_solution[0])
        s -= to_remove
        self.solve(n, s)
        self.filter_solution(to_remove)
        return self.prev_solution

    def get_common(self):
        if not self.prev_solution:
            print("no solutions yet: please solve first")
            return set()
        if len(self.prev_solution) == 1:
            # only one possible solution: do nothing
            return set()
        # first = set(self.prev_solution[0])
        # self.commons = first.intersection([set(sol) for sol in self.prev_solution[1:]])
        self.commons = set.intersection(*[set(sol) for sol in self.prev_solution])
        return self.commons

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
            if user_in[0] == 'f':
                solver.filter_solution(int(user_in[1]))
            elif user_in[0] == 'w':
                solver.winnow(int(user_in[1]))
            else:
                solver.solve(int(user_in[0]), int(user_in[1]))
            for sol in solver.prev_solution:
                print(sol)
        elif num_args == 1:
            if user_in[0] == 'c':
                solver.get_common()
                print(solver.commons)
        else:
            print("try n sum,")
            print("or q to quit")

if __name__ == "__main__":
    main()