#! /usr/bin/env python3
import sys

__author__ = "Akshay D. Nehe"
__purpose__ = "Check if a one-to-one character mapping can exist from string1 to string2"


def compare_strings(str1, str2):
    """
    Both strings are represented as strings.
    Core logic is to check whether unique characters in str1 are more than or equal to
    unique characters in str2.
    """

    set1 = set(str1)
    set2 = set(str2)
    if len(set1) >= len(set2):
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError('Expected 2 arguments: <str1> <str2>')

    compare_strings(str(sys.argv[1]), str(sys.argv[2]))
