#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(key, value, sep=': ') # like  hashmap in java hehe
