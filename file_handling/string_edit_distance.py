"""
Q-8: String Edit Distance.

Use your recursive function to write a program that reads two strings from the
user and displays the edit distance between them.

The edit distance between two strings is a measure of their similarity. The
smaller the edit distance, the more similar the strings are with regard to the
minimum number of insert, delete and substitute operations needed to transform
one string into the other.
"""


def edit_distance(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)

    if s[0] == t[0]:
        return edit_distance(s[1:], t[1:])

    insert = edit_distance(s, t[1:])
    delete = edit_distance(s[1:], t)
    replace = edit_distance(s[1:], t[1:])

    return 1 + min(insert, delete, replace)


print(edit_distance("kitten", "sitting"))
print(edit_distance("cat", "cut"))
