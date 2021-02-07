import unittest
from vector.vector import Vector
import time

class test_vector(unittest.TestCase):
    def test_int_vector_constructor_works(self):
        test_entries = [1,2,3]
        Vector(test_entries)

    def test_float_vector_constructor_works(self):
        test_entries = [1.23, 2.31, 3.12]
        Vector(test_entries)

    def test_float_int_vector_constructor_works(self):
        test_entries = [456, 123, 1.23]
        Vector(test_entries)

    def test_string_vector_constructor_fails(self):
        test_entries = ["abc", 123, 1.23]
        with self.assertRaises(TypeError):
            Vector(test_entries)
            
        

if __name__ == '__main__':
    unittest.main()