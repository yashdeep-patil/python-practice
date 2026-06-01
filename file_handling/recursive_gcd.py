"""
Q-7: Write a function that accepts two numbers and returns their greatest
common divisor. Without using any loop.

def gcd(int, int) => int

gcd(16, 24) will give 8
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(18, 136))
