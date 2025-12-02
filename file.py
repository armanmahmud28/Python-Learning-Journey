
import os

with open("test.txt", "w") as f:
    f.writelines(["Hello World!\n", "line2\n", "line3"])

with open("test.txt", "r") as f:
    n = f.read()

print(n)


file = "test.txt"

if os.path.exists(file):
    os.remove(file)
else:
    print("File not found!")
