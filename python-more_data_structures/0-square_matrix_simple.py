#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    
    Args:
        matrix: A 2-dimensional array of integers
        
    Returns:
        A new matrix of the same size as matrix with each value squared
    """
    # Create a new matrix using list comprehension
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    
    return new_matrix