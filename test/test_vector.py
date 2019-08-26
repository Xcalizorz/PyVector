import unittest

from vector.error.vector_zero_division_error import VectorZeroDivisionError
from vector.vectorcls import Vector

class Test2DimensionalVector(unittest.TestCase):
    """Testing our multidimensional Vector, using a 2 dimensional vector"""
    def setUp(self):
        self.test_2n_vector_1 = Vector(1, 2)
        self.test_2n_vector_2 = Vector(3, 4)
    
    def test_print_vector_2n(self):
        self.assertEqual(str(self.test_2n_vector_1), "Vector(1, 2)")

    def test_add_vectors_2n(self):
        expected_vector = Vector(4, 6)
        actual_vector = self.test_2n_vector_1 + self.test_2n_vector_2
        self.assertTupleEqual(actual_vector._data, expected_vector._data)

    def test_mult_vectors(self):
        expected_vector = Vector(3, 8)
        actual_vector = self.test_2n_vector_1 * self.test_2n_vector_2
        self.assertTupleEqual(actual_vector._data, expected_vector._data)

    def test_sub_vectors(self):
        expected_vector = Vector(-2, -2)
        actual_vector = self.test_2n_vector_1 - self.test_2n_vector_2
        self.assertTupleEqual(actual_vector._data, expected_vector._data)

    def test_div_vectors_normal(self):
        expected_vector = Vector((1/3), (2/4))
        actual_vector = self.test_2n_vector_1 / self.test_2n_vector_2
        self.assertTupleEqual(actual_vector._data, expected_vector._data)

    def test_div_vectors_div_by_zero(self):
        bad_vector = Vector(0, 1)
        with self.assertRaises(VectorZeroDivisionError):
            self.test_2n_vector_1 / bad_vector

    def test_len_vectors(self):
        self.assertEqual(2, len(self.test_2n_vector_1))
    
    def test_getitem_vectors(self):
        self.assertEqual(1, self.test_2n_vector_1[0])
    
    def test_bool_filled_vector(self):
        self.assertTrue(self.test_2n_vector_1)

    def test_bool_empty_vector(self):
        empty_vector = Vector(0, 0, 0, 0)
        self.assertFalse(empty_vector)
