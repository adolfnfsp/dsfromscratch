'''
more on vectors
'''
# componentwise sum a list of vectors
from typing import List

Vector = List[float]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

# multiply vector by a scalar

def scalar_multiply(c: float, v: Vector) -> Vector:
    """multiply every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

# allows us to compute componentwise means of a list

def vector_mean(vectors: List[Vector]) -> Vector:
    """Compute the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

# dot product

def dot(v: Vector, w: Vector) -> float:
    """Compute v_1 * w_1 + ...+ v_n * w_n"""
    assert len(v) == len (w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6
# with w of magnitude 1 (i.e., w = [1, 0]), dot product is projection of
# v onto w
# using this, it's easy to compute vector's sum of squares

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ...+ v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3

# which we can use to compute its magnitude (or length)

import math

def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v)) # math.sqrt is square root function

assert magnitude([3, 4]) == 5
# we now have all ingredients to compute distance between two vectors

def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ...+ (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))

# above is equivalent to:

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))

# Note: used heavily throughout this DS journey
# In production code, we would want to use NumPy library to get access
# to high-performance array class with all sorts of arithmetic operations


