"""
Q-10: Write a recursive function to convert a decimal to binary.
"""


def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


print(decimal_to_binary(10))
