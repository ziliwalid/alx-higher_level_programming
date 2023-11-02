#!/usr/bin/python3
"""describes multi of two matrices"""


def matrix_mul(m_a, m_b):
    """multiply two matrices, basically lots of work
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    i_b = []
    for i in range(len(m_b[0])):
        row = []
        for c in range(len(m_b)):
            row.append(m_b[c][i])
        i_b.append(row)

    nmatrice = []
    for row in m_a:
        NewRow = []
        for col in i_b:
            prod = 0
            for i in range(len(i_b[0])):
                prod += row[i] * col[i]
            NewRow.append(prod)
        nmatrice.append(NewRow)

    return 
