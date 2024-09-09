import unittest

import solver


class TestSolver(unittest.TestCase):

    def test_five_numbers(self):
        s = solver.Solver([5, 23, 35, 42, 7], 25)
        self.assertEqual(s.brute_solve(False)[1], 25)

        s.target = 2573
        # target is impossible to achieve so should return closest
        # which is 2576
        self.assertEqual(s.brute_solve(False)[1], 2576)

        s = solver.Solver([5, 231, 355, 422, 7213], 2573)
        self.assertEqual(s.brute_solve(False)[1], 2508)

