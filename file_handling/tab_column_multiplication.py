f = open('tab_column_multiplication.txt','w')
f.write('1   2\n3   4\n5   6\n7   8\n9   10\n')
total_sum = 0
f.close()

f = open('tab_column_multiplication.txt','r')
for line in f:
  line = line.strip().split()
  b = int(line[0]) * int(line[1])
  total_sum += b
  print(line[0],line[1],b)  
f.close()
print(total_sum)