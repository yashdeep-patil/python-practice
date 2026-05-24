f = open('vowel_count.txt','w')
f.write('hello my name is yashdeep uu')
f.close()

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
f = open('vowel_count.txt','r')
for line in f:
    for char in line:
        if char in vowels:
            vowels[char] += 1

print(vowels)
f.close()            