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

f1 = open ('reversed.txt', 'r')
print(f1.read())
f1.close()