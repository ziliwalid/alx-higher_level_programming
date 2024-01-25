#!/usr/bin/python3
"""elaborates peak-finding algorithm"""


def find_peak(list_of_integers):
    """ does some peak finding magic"""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    x = int(length / 2)
    Lints = list_of_integers

    if x - 1 < 0 and x + 1 >= length:
        return Lints[x]
    elif x - 1 < 0:
        return Lints[x] if Lints[x] > Lints[x + 1] else Lints[x + 1]
    elif x + 1 >= length:
        return Lints[x] if Lints[x] > Lints[x - 1] else Lints[x - 1]

    if Lints[x - 1] < Lints[x] > Lints[x + 1]:
        return Lints[x]

    if Lints[x + 1] > Lints[x - 1]:
        return find_peak(Lints[x:])
    return find_peak(Lints[:x])
