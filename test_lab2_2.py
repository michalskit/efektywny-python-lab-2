import unittest
import ast
import inspect
from lab2_2 import gaderypoluki


class TestGaderypoluki(unittest.TestCase):
    
    def test_gaderypoluki_example(self):
        self.assertEqual(gaderypoluki('Ala ma kota'), 'gug mg iptg')
        self.assertEqual(gaderypoluki('gug mg iptg'), 'ala ma kota')
    
    def test_gaderypoluki_custom(self):
        self.assertEqual(gaderypoluki('GADERYPOLUKI'), 'agedyropulik')
        self.assertEqual(gaderypoluki(''), '')
        self.assertEqual(gaderypoluki('Hello'), 'hduup')
        self.assertEqual(gaderypoluki('WORLD'), 'wpyue')
    
    def test_key_is_not_modified(self):
        source = inspect.getsource(gaderypoluki)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if target.id == 'key':
                        self.fail("Do not modify the 'key' argument in the function!")

if __name__ == '__main__':
    unittest.main()
