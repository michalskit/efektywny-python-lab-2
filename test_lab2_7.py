import unittest
from lab2_7 import powerset 

class TestPowersetFunction(unittest.TestCase):

    def test_empty_list(self):
        # Testowanie zachowania dla pustej listy
        self.assertEqual(set(frozenset(subset) for subset in powerset([])), {frozenset()})

    def test_single_character(self):
        # Testowanie zachowania dla listy z pojedynczym znakiem
        self.assertEqual(set(frozenset(subset) for subset in powerset(['a'])), {frozenset(), frozenset(['a'])})

    def test_multiple_characters(self):
        # Testowanie zachowania dla listy z wieloma znakami
        expected_result = {frozenset(), frozenset(['a']), frozenset(['b']), frozenset(['a', 'b']), frozenset(['c']), frozenset(['a', 'c']), frozenset(['b', 'c']), frozenset(['a', 'b', 'c'])}
        self.assertEqual(set(frozenset(subset) for subset in powerset(['a', 'b', 'c'])), expected_result)

    def test_numbers(self):
        # Testowanie zachowania dla listy z liczbami
        expected_result = {frozenset(), frozenset([1]), frozenset([2]), frozenset([1, 2]), frozenset([3]), frozenset([1, 3]), frozenset([2, 3]), frozenset([1, 2, 3])}
        self.assertEqual(set(frozenset(subset) for subset in powerset([1, 2, 3])), expected_result)

    def test_mixed(self):
        # Testowanie zachowania dla listy z różnymi typami danych
        expected_result = {frozenset(), frozenset(['abc']), frozenset([5]), frozenset(['abc', 5]), frozenset([6]), frozenset(['abc', 6]), frozenset([5, 6]), frozenset(['abc', 5, 6])}
        self.assertEqual(set(frozenset(subset) for subset in powerset(['abc', 5, 6])), expected_result)

    def test_repeated_elements(self):
        # Testowanie zachowania dla listy z powtarzającymi się elementami
        expected_result = {frozenset(), frozenset([1])}
        self.assertEqual(set(frozenset(subset) for subset in powerset([1, 1])), expected_result)


if __name__ == '__main__':
    unittest.main()


