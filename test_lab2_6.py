import unittest
import ast
import inspect
from lab2_6 import func1, func2


class TestGenerators(unittest.TestCase):

    def assert_contains_yield(self, func):
        tree = ast.parse(inspect.getsource(func))
        for node in ast.walk(tree):
            if isinstance(node, ast.Yield):
                return
        raise AssertionError(f"Function {func.__name__} does not use yield.")

    def test_func1_yields(self):
        self.assert_contains_yield(func1)

    def test_func2_yields(self):
        self.assert_contains_yield(func2)

    def test_func1(self):
        n = 3
        expected = [(1, 1), (1, 2), (2, 1), (2, 2)]
        self.assertEqual(list(func1(n)), expected)

    def test_func2(self):
        n = 4
        expected = [(1, 2), (1, 3), (2, 3)]
        self.assertEqual(list(func2(n)), expected)

    def test_func1_large(self):
        n = 100
        self.assertEqual(len(list(func1(n))), (n - 1) ** 2)

    def test_func2_large(self):
        n = 100
        # Sum of the first n-2 natural numbers
        expected_count = (n - 2) * (n - 1) // 2
        self.assertEqual(len(list(func2(n))), expected_count)


if __name__ == "__main__":
    unittest.main()
