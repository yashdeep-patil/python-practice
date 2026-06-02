f = open("file.txt" , "w")
f.write("how are you,kese ho sir")
f.close()

try:
    f = open("giu.txt" , "r")
    s = f.readlines()
    print(s[-1].strip())

except FileNotFoundError:
    print("chala ja bsdk")

finally:
    f.close()