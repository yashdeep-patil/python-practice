"""
Q-1: Write a function get_final_line(filename), which takes filename as input
and returns the final line of the file.

Note: You can choose any file of your choice.
"""

f = open('note.txt', 'w')
f.write('Hello')
f.write('\npython')
f.write('\nFile Handling')
f.close()

f = open('note.txt', 'r')
s = f.readlines()
print(s[-1].strip())
f.close()
