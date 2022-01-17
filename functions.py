# import sys
# try: 
#   number = int(sys.argv[1])
# except IndexError:
#   print("Тоо оруулна уу")
# !n = n*(n-1)*(n-2)...*2*1
# 7!=7*6*5*4*3*2*1=5040

# def factorial(number):
#   result = number
#   try: 
#     assert number >= 0 and number == int(number)
#   except AssertionError:
#     return "Cөрөг эсвэл бутархай тоо оруулж болохгүй." 
  
#   while number > 1:
#     number -= 1
#     result = result * number
#   return result 
# print(factorial(7))



# def recursive_factorial(n):
#   assert n >= 0 and n == int(n), "error" 
#   if n in [0, 1]:
#     return 1
#   else:
#     return n * recursive_factorial(n-1)
  # return number * (number - 1)

# print(recursive_factorial(number))


# def fibonnaci(n):
#   if n in [0, 1]:
#     return n
#   else:
#     return fibonnaci(n-1) + fibonnaci(n-2)


# нийл олох
# def total(n):
#   if n in [0, 1]:
#     return 1
#   return n + total(n-1)

# import glob
# import os

# path = os.getcwd()

# for name in glob.glob(f'{path}/*.py'):
#     print(name)

# def power(base, exp):
#   assert exp >= 0 and exp == int(exp), "Cөрөг эсвэл бутархай тоо оруулж болохгүй."
#   if exp == 0:
#     return 1
#   if exp == 1:
#     return base
#   return base * power(base, exp - 1)

# print(power(2, -1))
import playsound

class Dog:

  def __init__(self, name, age, color, sound):
      self.name = name
      self.age = age
      self.color = color
      self.sound = sound

  def bark(self):
    print("she is barking")
    return playsound.playsound(f'{self.sound}.mp3', True)

  def __str__(self):
    return f"{self.name} is {self.age} years old, {self.color}"
dog1 = Dog("Penny", 2, "brown", 1)
dog2 = Dog("Jenny", 5, "white", 2)
import sys
num = int(sys.argv[1])
def show(num):
  if (num == 1):

    print(str(dog1))
    dog1.bark() 
  if (num == 2):
    print(str(dog2))
    dog2.bark() 

show(num)