# -*- coding: utf-8 -*-
"""sunday.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XmWdMh35lo3Coy6mgrtFfTpIlhgjW5IW
"""

#menus
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
'''

'''
a = int (input ("Kindly enter 1st number"))
b =int(input ("kindly enter 2nd number"))

c = a+b
d = a-b
e = a*b
f = a/b

print ("addition of two number is",c)
print ("product of two number is",d)
'''
'''
a= int (input ("kindly enter the integer"))
b= float (input ("kindly enter the float"))
c= str (input("kindly enter the string"))
d= a>b

print ("a is {}, b is {}, c is {} and value of d is {}". format (a,b,c,d))

#Nested
a = int (input ("Enter A: "))
b = int (input ("Enter B: "))
c = int (input ("Enter C: "))

if (a>b):
  if  (a>c):
    print ("A is greatest")
  else:
    print ("C is greater than A")
    
  else:
    if (b>c):
      print ("B is greatest")
  else:
    print ("C is the greatest")

x = int (input ("Enter X: "))
y = int (input ("Enter Y: "))
z = int (input ("Enter Z: "))

if (x>y):
  if (z==x):
    print ("lol")
  
else:
  if (x<y):
    if (z!=x):
      print ("dlol")