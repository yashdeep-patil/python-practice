"""
Q-6: Given a string calculate length of the string using recursion.

Example 1:
Input: "abcd"
Output: 4

Example 2:
Input: DataScience
Output: 11
"""


def length(s):
    if s == "":
        return 0
    else:
        print(s[1:])
        return 1 + length(s[1:])


print(length("abcd"))
print(length("DataScience"))
