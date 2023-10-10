import unittest
from collections import Counter
from lab2_1 import check_anagram


class TestAnagram(unittest.TestCase):
    
    def test_given_examples(self):
        self.assertTrue(check_anagram("abcd", "dcba"))
        self.assertTrue(check_anagram("aba", "baa"))
        self.assertFalse(check_anagram("aba", "ba"))
        self.assertTrue(check_anagram("tom marvolo riddle", "i am lord voldemort"))
    
    def test_edge_cases(self):
        # Testy z pustymi stringami
        self.assertTrue(check_anagram("", ""))
        self.assertFalse(check_anagram("a", ""))
        self.assertFalse(check_anagram("", "b"))
        
        # Test z różnymi wielkimi literami
        self.assertFalse(check_anagram("A", "a"))
        self.assertTrue(check_anagram("Aa", "aA"))
        
        # Test z różnymi białymi znakami
        self.assertTrue(check_anagram(" ab c ", "c ba"))
        self.assertTrue(check_anagram("ab c", "c b a"))
        
        # Test z długimi stringami, które nie są anagramami
        long_string1 = "a" * 1000 + "b"
        long_string2 = "a" * 1001
        self.assertFalse(check_anagram(long_string1, long_string2))
        
    def test_same_input(self):
        # Jeżeli input jest taki sam, to muszą być anagramami
        self.assertTrue(check_anagram("apple", "apple"))
        self.assertTrue(check_anagram("   a    b    ", " a b "))

if __name__ == "__main__":
    unittest.main()
