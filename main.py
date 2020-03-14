#! /usr/bin/env python3
import sys

__author__ = "Akshay D. Nehe"
__purpose__ = "Check if a one-to-one character mapping can exist from string1 to string2"

# TODO Raise an exception instead of simply exiting
if len(sys.argv) != 3:
    print('Expected 2 arguments: <str1> <str2>')
    exit(1)


# TODO Write as a function
str1 = str(sys.argv[1])
len1 = len(str1)
dict1 = dict()
str2 = str(sys.argv[2])
len2 = len(str2)
dict2 = dict()

larger_length = max(len1, len2)

for idx in range(larger_length):
    if idx < len1:
        dict1[str1[idx]] = dict1.get(str1[idx], 0) + 1
    elif len(dict2.keys()) > len(dict1.keys()):
        break
    if idx < len2:
        dict2[str2[idx]] = dict2.get(str2[idx], 0) + 1
    elif len(dict2.keys()) <= len(dict1.keys()):
        break

result = 'true' if len(dict2.keys()) <= len(dict1.keys()) else 'false'
print(result)
