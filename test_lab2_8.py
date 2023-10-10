import unittest
import ast
import inspect
from lab2_8 import primes_extra


class TestPrimesFunction(unittest.TestCase):

    def test_function_content(self):
        source_code = inspect.getsource(primes_extra)
        parsed_code = ast.parse(source_code)
        
        for node in ast.walk(parsed_code):
            if isinstance(node, (ast.For, ast.While)):
                self.fail("Found prohibited loop in the code!")
            if isinstance(node, (ast.GtE, ast.LtE)):
                self.fail("Found prohibited operator in the code!")

    def test_output(self):
        self.assertEqual(primes_extra(0), set())
        self.assertEqual(primes_extra(1), set())
        self.assertEqual(primes_extra(2), {2})
        self.assertEqual(primes_extra(3), {2, 3})
        self.assertEqual(primes_extra(5), {2, 3, 5})
        self.assertEqual(primes_extra(10), {2, 3, 5, 7})
        self.assertEqual(primes_extra(20), {2, 3, 5, 7, 11, 13, 17, 19})

if __name__ == "__main__":
    unittest.main()
