from math import hypot
from operator import add, mul, sub, truediv

from vector.error.vector_zero_division_error import VectorZeroDivisionError


class Vector:
    def __init__(self, *args):
        self.dimension = len(args)
        self._data = args
    
    def __repr__(self):
        str_data = [str(arg) for arg in self._data]
        return "Vector(" + ", ".join(str_data) + ")"

    def _generate_new_parameter_list(self, other, func):
        new_parameter_list = []
        for self_parameter, other_parameter in zip(self._data, other._data):
            new_value = func(self_parameter, other_parameter)
            new_parameter_list.append(new_value)
        return Vector(*new_parameter_list)    

    def __bool__(self):
        return bool(sum(self._data))

    def __add__(self, other):
        return self._generate_new_parameter_list(other, add)
    
    def __mul__(self, other):
        return self._generate_new_parameter_list(other, mul)

    def __truediv__(self, other):
        try:
            return self._generate_new_parameter_list(other, truediv)
        except ZeroDivisionError:
            raise VectorZeroDivisionError

    def __sub__(self, other):
        return self._generate_new_parameter_list(other, sub)

    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, position):
        return self._data[position]
