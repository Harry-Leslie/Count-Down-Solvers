from typing import List
import itertools
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Solver:
    def __init__(self, arr: List[int], target: int):
        self.arr = arr
        self.target = target
        self.operators = ['+', '-', '*', '/']

    def brute_solve(self, verbose: bool) -> tuple:
        """
        Find the closest solution to the target by going through all possible
        combinations of solution using brute force. If multiprocessing_flag is True,
        parallelize the evaluation process.
        :param multiprocessing_flag: whether to use multiprocessing for evaluation.
        :param verbose: whether to log detailed steps during execution.
        :return: a tuple with the expression string closest to the target and the value.
        """
        combination_array: List[List[int]] = []

        logger.info("Starting Brute Force Solve")

        # Gets all the different combinations of the number and then collects all the permutations of each
        for combination in self.all_number_combinations(self.arr):
            combination_array.extend([list(tup) for tup in itertools.permutations(combination, len(combination))])

        logger.info("Computed all number combinations and permutations")

        if verbose:
            print(f"The list of combinations and permutations: {combination_array}")

        all_expressions_without_brackets: List[List[object]] = []
        for combination in combination_array:
            all_expressions_without_brackets.extend(self.all_possible_operator_lists(combination))

        logger.info("Computed all mathematical expressions (without brackets)")
        if verbose:
            print(f"The list of all mathematical expressions (without brackets): {all_expressions_without_brackets}")

        all_possible_expressions: List[List[object]] = []
        for expression in all_expressions_without_brackets:
            all_possible_expressions.extend(self.selective_bracketing(expression))
        logger.info("Computed all possible expressions")
        if verbose:
            print(all_possible_expressions)

        stringify_list: List[str] = []
        for expression in all_possible_expressions:
            stringified_list: List[str] = []
            for char in expression:
                stringified_list.append(str(char))
            stringify_list.append(''.join(stringified_list))

        current_best = float('inf')
        current_eval = 'None'

        all_best_solutions = []

        for expr in stringify_list:
            try:
                result = eval(expr)
                if result == self.target:
                    return expr, self.target, [expr]
                if (abs(result - self.target) < abs(current_best - self.target)
                        and eval(expr) // 1 == eval(expr)):
                    current_eval = expr
                    current_best = result
                    all_best_solutions = [expr]
                elif (abs(result - self.target) == abs(current_best - self.target)
                        and eval(expr) // 1 == eval(expr)):
                    all_best_solutions.append(expr)

            except ZeroDivisionError:
                continue

        return current_eval, int(current_best), all_best_solutions

    @staticmethod
    def all_number_combinations(arr: List[int]) -> List[List[int]]:
        """
        Gets all possible number combinations.
        :return: a list of all combinations of the provided numbers.
        """
        all_combinations_of_numbers = []
        for r in range(1, len(arr) + 1):
            all_combinations_of_numbers.extend(
                [list(tup) for tup in list(itertools.combinations(arr, r))]
            )
        return all_combinations_of_numbers

    def all_possible_operator_lists(self, arr: List[int]) -> List[List[object]]:
        """
        Produces all possible operator combinations with the numbers provided.
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

    def selective_bracketing(self, expr: List[object]) -> List[List[object]]:
        """
        A more efficient way of adding brackets to the expression.
        Focus on applying brackets where necessary (for *, /) and avoid
        unnecessary combinations that don't impact the result significantly.

        :param expr: A list of numbers and operators.
        :return: A list of possible expressions with selective bracketing.
        """
        result = [expr]  # Start with no brackets
        operators = [op for i, op in enumerate(expr) if isinstance(expr[i], str)]

        # Only consider adding brackets for expressions with mixed precedence
        if '*' in operators or '/' in operators:
            result.extend(self.add_bracketing(expr))

        return result

    def add_bracketing(self, expr: List[object]) -> List[List[object]]:
        """
        Finds all possible ways of bracketing an array.
        """
        if len(expr) == 1:
            return [expr]

        result = []

        for i in range(1, len(expr) - 1, 2):
            left_part = self.add_bracketing(expr[:i])
            right_part = self.add_bracketing(expr[i + 1:])

            for left in left_part:
                for right in right_part:
                    result.append(['('] + left + [expr[i]] + right + [')'])

        return result
