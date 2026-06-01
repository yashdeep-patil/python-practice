"""
Q-2: Read through a text file, line by line. Use a dict to keep track of how
many times each vowel (a, e, i, o, and u) appears in the file. Print the
resulting tabulation dictionary.
"""

f = open('vowel_count.txt', 'w')
f.write('hello my name is yashdeep')
f.close()

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

f = open('vowel_count.txt', 'r')

for line in f:
    for char in line:
        if char in vowels:
            vowels[char] += 1

print(vowels)

f.close()
