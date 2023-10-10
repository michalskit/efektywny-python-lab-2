import unittest
import ast
import inspect
from lab2_3 import comprehensions_even_numbers_from_list, comprehensions_words_analyze, \
    comprehensions_count_words_starting_with_given_letter


class TestComprehensionsFunctions(unittest.TestCase):

    def test_comprehensions_even_numbers_from_list(self):
        self.assertEqual(comprehensions_even_numbers_from_list([1, 2, 3, 4]), [2, 4])
        self.assertEqual(comprehensions_even_numbers_from_list(range(10)), list(range(0, 10, 2)))
        self.assertEqual(comprehensions_even_numbers_from_list(range(1000)), list(range(0, 1000, 2)))
        self.assertEqual(comprehensions_even_numbers_from_list([10, 2, 3, 4, 6, -3, -4]), [10, 2, 4, 6, -4])

    def test_comprehensions_words_analyze(self):
        self.assertEqual(comprehensions_words_analyze(['tomek', 'jadzia']), [(0, 'tomek', 5), (1, 'jadzia', 6)])
        self.assertEqual(comprehensions_words_analyze([]), [])

    def test_comprehensions_count_words_starting_with_given_letter(self):
        self.assertEqual(comprehensions_count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'o'),
                         {'ola': 2, 'o': 1})
        self.assertEqual(comprehensions_count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'k'),
                         {'kota': 1})
        self.assertEqual(comprehensions_count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'x'),
                         {})

    # Dodatkowy test sprawdzający, czy funkcje używają comprehensions
    def test_functions_use_comprehensions(self):

        def check_comprehension(node):
            for n in ast.walk(node):
                if isinstance(n, (ast.ListComp, ast.DictComp, ast.SetComp)):
                    return True
            return False

        for func in [comprehensions_even_numbers_from_list, comprehensions_words_analyze,
                    comprehensions_count_words_starting_with_given_letter]:
            source_code = inspect.getsource(func)
            self.assertTrue(check_comprehension(ast.parse(source_code)))


if __name__ == "__main__":
    unittest.main()
