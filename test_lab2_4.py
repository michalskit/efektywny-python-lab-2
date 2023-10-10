import unittest
import inspect
import ast
from lab2_4 import comprehensions_merge_dicts, add


class TestComprehensionsMergeDicts(unittest.TestCase):
    def test_comprehensions_merge_dicts(self):
        self.assertEqual(comprehensions_merge_dicts({'a': 1}, {'b': 1}, add), {'b': 1, 'a': 1})
        self.assertEqual(comprehensions_merge_dicts({'a': 1, 'b': 2}, {'b': 1}, add), {'b': 3, 'a': 1})
        self.assertEqual(comprehensions_merge_dicts({'a': 1, 'b': 2}, {'b': 1, 'c': 3, 'a': 7}, add), {'c': 3, 'b': 3, 'a': 8})


    def test_function_uses_comprehension(self):
        source_code = inspect.getsource(comprehensions_merge_dicts)
        tree = ast.parse(source_code)
        
        # Sprawdzenie, czy w drzewie AST funkcji istnieją węzły typu ListComp, DictComp lub SetComp
        uses_comprehension = any(isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp)) for node in ast.walk(tree))

        self.assertTrue(uses_comprehension, msg="Function does not use comprehension!")


if __name__ == "__main__":
    unittest.main()
