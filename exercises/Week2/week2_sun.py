# -*- coding: utf-8 -*-
"""Week2-sun.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JTZMImcYfIMtW42nrHK4MLLUZ91cnntZ
"""

# Driver Code
compound_interest(10000, 10.25, 5)


num = int(input("enter a number: "))

length = len(str(num))
sum = 0
temp = num

while (temp != 0):
    sum = sum + ((temp % 10) ** length)
    temp = temp // 10

if sum == num:
    print("armstrong number")
else:
    print("not armstrong number")
'''
'''
# Python program to find Area of a circle

def findArea(r):
	PI = 3.142
	return PI * (r*r);

# Driver method
print("Area is %.6f" % findArea(5));



# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")

#fibonacci
num = int(input("enter number of digits you want in series (minimum 2): "))

first = 0
second = 1

print("\nfibonacci series is:")
print(first, ",", second, end=", ")

for i in range(2, num):
    next = first + second
    print(next, end=", ")

    first = second
    second = next



# Python program to find the sum of natural numbers up to n where n is provided by user

# change this value for a different result
num = 18

# uncomment to take input from the user
#num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)
'''
'''
# Python3 code to find
# the area of the square

def areaSquare( side ):
	area = side * side
	return area

# Driver Code
side = 4
print(areaSquare(side))
'''
'''
a = int (input ("enter your number"))
print (a)
if (a%2 == 0):
    print ("even")
else:
    print ("odd")
'''
'''
a = 5
b = 2

c = a//b
print(c)
'''
'''
a = 10
b = 10

c = (a==b)
print (type(c))
'''
'''
a = int (input ("enter your number"))
b = int (input ("enter your number"))
c = int (input ("enter your number"))

if (a==b & b==c):
  print (ullu)

else:
  print (none)
'''
'''
x = [1,2,3,4,5,6,7,8,9,20]
y = ["ram", 2, "love", "u"]
#b = y[0] + y[2] + y[3] + y[1]
print (y[0] \n y[2] \n y[3])
'''
'''
name = str (input ("enter your name"))
age = int (input ("enter your age"))
hobby = str (input ("enter your hobby"))
gender = str (input ("enter your gender"))
x = name + "is" + gender
print (x)

print ("this invidual name is {}, age is {}, hobby is {} gender is {}".format(name,age,hobby,gender) )
'''
'''
name = str (input ("what is your name"))
n_m = name[0:1:5]
print (n_m)
'''
'''
name = str (input ("what is your name"))
n_m = name[0:3]
print ((n_m) + "z")
'''
'''
name = str (input ("what is your name"))
n_m = name[0:3:4]
print (n_m)
'''
'''
name = str (input ("what is your name"))
y = str("kindly enter your prefix for eg 0,1,2,3:")
z = int (input ("enter number of your initials"))
print (x[0:3]+z)
'''
'''
#1.) Write a python Program to Add ,Multiply, Divide & Substract two numbers

a = int(input("kindly enter your number"))
b = int(input("kindly enter your second number"))
#please choose operator
z = a+b
x = a*b
y = a/b
w = a-b


print ("addition of two number is",z)
print ("addition of two number is",x)
print ("addition of two number is",y)
print ("addition of two number is",w)
'''
'''
a = str(input("kindly enter your month"))
b = str(input("please enter your name"))
c = str(input("please enter your DOB"))
d = int(input("add current year"))

print (x[5:8])
    if (a = "january", "march", "may", "july", "august", "october", "december"):
        print (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31):
    elif a = "february":
            print (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28):
    else (a = "april", "june", september, november):
        print (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30):
'''
'''
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]:

for i in x:
    print (i)
'''
'''
def sum(a,b):
    c = a+b
    return (c)
sum(5,6)
'''

def Cntn (n):
  x = str(input("Kindly enter your name"))
  y = str(input("kindly enter your prefix for eg 0,z,o,u"))
  z = int(input("enter number of your initials:"))
  cntn ("Nitin")
  print (x[0:z]+y)