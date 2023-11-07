#!/usr/bin/python3
"""
read_file function
"""


def read_file(filename=""):
    """""reads a text file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
