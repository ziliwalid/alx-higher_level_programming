#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nDict = a_dictionary.copy()
    for key, value in list(nDict.items()):
        nDict[key] = value * 2
    return nDict
