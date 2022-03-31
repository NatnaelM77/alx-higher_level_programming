#!/usr/bin/python3
"""Module for to_json_string function."""
import json


def to_json_string(my_obj):
    """This function return the object serialized by json."""
    return json.dumps(my_obj)
