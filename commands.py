import sys
import operator
import math as m

m.pi


format(ord("A"), "08b")
# '01000001'
letter = format(ord("A"), "08b")
sys.getsizeof(letter)
# 57 because it contains additional infos e.g length
a = "a"
# actual size of a letter
sys.getsizeof(a + "a") - sys.getsizeof(a)



def hello(num):
  num -= 1
  if num < 0:
    print("over")
    return
  print(num)
  return hello(num)

hello(100)


import os

cwd = os.listdir(os.getcwd()) # list, current directory names
os.system("touch hello.txt")
os.system("echo 'hello world' > hello.txt")
os.system("open hello.txt")


commands = ["touch hello.txt", "echo 'test' > hello.txt", "open hello.txt"]

for command in commands:
  os.system(command)

with open("hello.txt", "w") as f:
  for num in range(10): 
    f.write(f"hello world {num + 1}\n")



