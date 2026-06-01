"""
Q-9: Run-Length Encoding.

Run-length encoding is a simple data compression technique that can be
effective when repeated values occur at adjacent positions within a list.
Compression is achieved by replacing groups of repeated values with one copy
of the value, followed by the number of times that the value should be
repeated.

Write a recursive function that implements the run-length compression
technique described above. Your function will take a list or a string as its
only parameter. It should return the run-length compressed list as its only
result.
"""


def run_length_encoding(s):
    if s == []:
        return []

    first_element = s[0]
    count = 0
    for element in s:
        if element == first_element:
            count += 1
        else:
            break

    return [first_element, count] + run_length_encoding(s[count:])


test_list = [
    "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "c",
    "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"
]
print(run_length_encoding(test_list))
