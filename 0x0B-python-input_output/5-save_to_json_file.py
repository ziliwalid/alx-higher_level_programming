#!/usr/bin/python3
"""
save_to_json_fille function
"""

import json


def save_to_json_file(my_obj, filename):
    """obj to txt"""
    with open(filename, 'w', encoding='utf-8') as fl:
        json.dump(my_obj, fl)
