from typing import List

"""
The Number Game (Countdown)

The number game involve 5 numbers a target. The aim of the game, is to get as 
close to the target as you can using four functions (+, -, *, /). 
You can not make the number negative or fractional at any point during the game.

This solver attempts to find the best solution possible
"""
class Solver:
    def __init__(self, arr: List[int], target: int):
        self.arr = arr
        self.target = target

    def brute_solve(self, verbose: bool) -> str:
        """
        Find the closest solution to the target by going through all possible
        combinations of solution

        Explanation:

        :returns: a string with a solution closest to the target
        """


    


