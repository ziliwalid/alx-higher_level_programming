#!/usr/bin/python3
"""
load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """loadds from a json file """
    with open(filename, 'r', encoding='utf-8') as fl:
        return json.load(fl)
