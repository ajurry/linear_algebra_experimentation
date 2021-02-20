import unittest
import time

from vector.vector import Vector

class test_vector(unittest.TestCase):

    def test_int_vector_constructor_works(self):
        Vector([1,2,3])

    def test_float_vector_constructor_works(self):
        Vector([1.23, 2.31, 3.12])

    def test_float_int_vector_constructor_works(self):
        Vector([456, 123, 1.23])

    def test_string_vector_constructor_fails(self):
        with self.assertRaises(TypeError):
            Vector(["abc", 123, 1.23])

    def test_length_of_vector(self):
        test_entries = [1,2,3]
        test_vector = Vector(test_entries)
    
        self.assertEqual(len(test_entries), len(test_vector))
                

    def test_get_entry_from_vector_with_valid_index(self):
        test_entries = [1,2,3]
        test_vector = Vector(test_entries)

        for index in range(0, len(test_entries)):
            self.assertEqual(test_entries[index], test_vector[index])

    def test_get_entry_from_vector_with_negative_index(self):
        test_vector = Vector([1,2,3])
        with self.assertRaises(IndexError):
            test_vector[-1]

    def test_get_entry_from_vector_with_out_of_range_index(self):
        test_vector = Vector([1,2,3])
        with self.assertRaises(IndexError):
            test_vector[len(test_vector)]
            
    def test_set_item_with_valid_data(self):
        test_update_entries = [4,5,6]
        test_vector = Vector([1,2,3])

        for index in range(0, len(test_update_entries)):
            test_vector[index] = test_update_entries[index]
            self.assertEqual(test_vector[index], test_update_entries[index])

    def test_set_item_with_too_large_an_index(self):
        test_vector = Vector([1,2,3])

        with self.assertRaises(IndexError):
            test_vector[len(test_vector)] = 100

    def test_set_item_with_negative_index(self):
        test_vector = Vector([1,2,3])

        with self.assertRaises(IndexError):
            test_vector[-1] = 100

    def test_set_item_with_invalid_data_type(self):
        test_vector = Vector([1,2,3])
        with self.assertRaises(TypeError):
            test_vector[2] = "abc"
        
    def test_append_vector_to_vector(self):
        # Hmmmm... I don't understand why test_vector_to_append
        # is becoming 4, 5, 6, 4, 5, 6
        # Surely, it should be 1, 2, 3, 4, 5, 6
        # Do not know why these objects are beind distinct
        test_vector_to_append = Vector([1,2,3])
        test_appendage = Vector([4,5,6])
        length_before = len(test_vector_to_append) + len(test_appendage)

        test_vector_to_append.append(test_appendage)
        self.assertEqual(len(test_vector_to_append), length_before)

        for index in range(0, len(test_appendage)):
            self.assertEqual(
                test_vector_to_append[len(test_appendage) + index],
                test_appendage[index]
                )
            

    def test_append_int_to_vector(self):
        test_vector_to_append = Vector([1,2,3])
        test_appendage = 4
        length_before = len(test_vector_to_append) + 1

        test_vector_to_append.append(test_appendage)
        self.assertEqual(len(test_vector_to_append), length_before)
        self.assertEqual(
            test_vector_to_append[len(test_vector_to_append) - 1],
            test_appendage
            )

    def test_append_float_to_vector(self):
        test_vector_to_append = Vector([1,2,3])
        test_appendage = 4.5
        length_before = len(test_vector_to_append) + 1

        test_vector_to_append.append(test_appendage)
        self.assertEqual(len(test_vector_to_append), length_before)
        self.assertEqual(
            test_vector_to_append[len(test_vector_to_append) - 1],
            test_appendage
            )

    def test_append_with_invalid_type(self):
        test_vector_to_append = Vector([1,2,3])
        test_appendage = "ABC"

        with self.assertRaises(TypeError):
            test_vector_to_append.append(test_appendage)

if __name__ == '__main__':
    unittest.main()