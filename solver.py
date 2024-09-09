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

        :returns: a string with a solution closest to the target, the number closest to the target
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

    def all_possible_operator_lists(self, arr: List[int]) -> List[List[object]]:
        """
        Produces all possible operator combinations with the numbers provided. :param arr: the array that you would
        like to add operators to in [number, opp, number ..., number] fashion :return: an array containing the list
        of numbers in [number, opp, number, ..., number] for all operators in self.operators
        """
        return self.all_possible_operator_lists_helper(arr, 0, [], [])

    def all_possible_operator_lists_helper(self, arr: List[int], current_index: int, current: List[object],
                                           res: List[List[object]]):
        if current_index >= len(arr) - 1:
            current.append(arr[current_index])
            res.append(current.copy())
            return res
        for operator in self.operators:
            temp = current.copy()
            temp.extend([arr[current_index], operator])
            self.all_possible_operator_lists_helper(arr, current_index + 1, temp, res)
        return res
