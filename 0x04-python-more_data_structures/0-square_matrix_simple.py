#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = matrix.copy()
    for rowCount in range(len(newMatrix)):
        newMatrix[rowCount] = list(map(lambda x: x ** 2, newMatrix[rowCount]))
    return newMatrix
