import unittest
import ast
import inspect
from lab2_5 import primes


class TestPrimesFunction(unittest.TestCase):

    def test_primes_function(self):
        self.assertEqual(primes(5), {2, 3, 5})
        self.assertEqual(primes(10), {2, 3, 5, 7})
        self.assertEqual(primes(100), {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})

    def test_primes_uses_comprehension(self):
        source = inspect.getsource(primes)
        tree = ast.parse(source)
        comprehensions = [node for node in ast.walk(tree) if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp))]
        self.assertTrue(comprehensions, "Function does not use comprehensions.")

    def test_functions_uses_comprehension_in_name(self):
        for name, func in inspect.getmembers(self, predicate=inspect.isfunction):
            if "comprehension" in name:
                source = inspect.getsource(func)
                tree = ast.parse(source)
                comprehensions = [node for node in ast.walk(tree) if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp))]
                self.assertTrue(comprehensions, f"Function {name} does not use comprehensions.")


if __name__ == '__main__':
    unittest.main()
