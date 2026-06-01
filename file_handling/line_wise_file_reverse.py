"""
Q-4: Create line wise reverse of a file.

Write a function which takes two arguments: the names of the input file
(to be read from) and the output file (which will be created).

For example, if a file looks like:
abc def
ghi jkl

then the output file will be:
fed cba
lkj ihg

Notice: The newline remains at the end of the string, while the rest of the
characters are all reversed.
"""

f = open('file.txt', 'w')
f.write('abc def\n')
f.write('ghi jkl\n')
f.close()

f = open('file.txt', 'r')
f1 = open('reversed.txt', 'w')

for line in f:
    line = line.strip()
    f1.write(line[::-1] + '\n')

f.close()
f1.close()

f1 = open('reversed.txt', 'r')
print(f1.read())
f1.close()
