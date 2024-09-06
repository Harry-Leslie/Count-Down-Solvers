from typing import List
import itertools

"""
The Number Game (Countdown)

The number game involve 5 numbers and a target. The aim of the game, is to get as 
close to the target as you can using four functions (+, -, *, /) and 
the 5 numbers (not necessarily all of them).

You can not make the number negative or fractional at any point during the calculation

This solver attempts to find the best solution possible.
"""


class Solver:
    def __init__(self, arr: List[int], target: int):
        self.arr = arr
        self.target = target

    def brute_solve(self, verbose: bool) -> str:
        """
        Find the closest solution to the target by going through all possible
        combinations of solution

        Explanation: Brute force solution.e This involves finding all
        combinations of permutations

        ie [1, 2, 3, 4, 5] are the numbers

        then ([1, opp, 2, opp, 3, opp, 4, opp, 5]) but you can also have
        combinations like [1, opp, 2, opp, 3] which could evaluate
        to the solution as well.

        Furthermore, you can have issues with bracketing because of BIDMAS.
        This means [1, opp, 2, opp 3] evaluates differently depending on the
        brackets positioning (ie [1, opp, (2, opp, 3)] vs [(1, opp, 2), opp, 3)] vs [(1, opp, 2, opp 3)]).

        Finally, because you do not need to use all the numbers, you need to check all combinations with
        bracketing - meaning addition computation is required.

        :return: a string with a solution closest to the target
        """

    def all_number_combinations(self):
        """
        Gets all possible number combinations which could
        add up to the target.

        :return: a list of all the combination of the provided numbers
        """

        all_combinations_of_numbers = []

        for r in range(1, len(self.arr)+1):
            all_combinations_of_numbers.extend(
                [list(tup) for tup in list(itertools.combinations(self.arr, r))]
            )

        return all_combinations_of_numbers
