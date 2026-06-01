"""
Q-3: Create a text file containing two tab separated columns, with each column
containing a number. Then use Python to read through the file created. For each
line, multiply each first number by the second and include it in the file in a
third column. In last add a line Total, by summing the value of third column.

Input File example:
1   2
3   4
5   6
7   8
9   10

Output File example:
1   2   2
3   4   12
5   6   30
7   8   56
9   10  90
Total   190
"""

f = open('tab_column_multiplication.txt', 'w')
f.write('1   2\n3   4\n5   6\n7   8\n9   10\n')
f.close()

total_sum = 0

f = open('tab_column_multiplication.txt', 'r')

for line in f:
    line = line.strip().split()

    b = int(line[0]) * int(line[1])

    total_sum += b

    print(line[0], line[1], b)

f.close()

print("Total =", total_sum)
