#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     22-01-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#---------------CALCULATOR (mini project)


print("----A Calculator for 2 inputs----\n")
operation=input("Enter which operation you want to perform out of the following options: \n1.Add \n2.Subtract \n3.Multiply \n4.Divide \n5.To the power \n6.Squareroot \n\n")



def add(a,b):
    print("\nThe Sum of ", a , " and ",b," is : ",a+b)
def sub(a,b):
    if a>=b:
        print("\nThe difference between ", a , " and ",b," is : ",a-b)
    elif a<b:
        print("\nThe difference between ", a , " and ",b," is : ",b-a)
def mul(a,b):
    print("\nThe product of ", a , " and ",b," is : ",a*b)
def div(a,b):
    print("\n We get ", a/b , " when we divide ",a ," by ", b)
def pwr(a,b):
    print("\n",a," to the power of ",b," gives: ", a**b)
def sqrt(a):
    print("The squareroot of ",a," is: ", a**(1/2))

if operation=='1':
    first_number=int(input("\nEnter the first number: "))
    second_number=int(input("\nEnter the second number: "))
    add(first_number,second_number)
elif operation=='2':
    first_number=int(input("\nEnter the first number: "))
    second_number=int(input("\nEnter the second number: "))
    sub(first_number,second_number)
elif operation=='3':
    first_number=int(input("\nEnter the first number: "))
    second_number=int(input("\nEnter the second number: "))
    mul(first_number,second_number)
elif operation=='4':
    first_number=int(input("\nEnter the first number: "))
    second_number=int(input("\nEnter the second number: "))
    div(first_number,second_number)
elif operation=='5':
    first_number=int(input("\nEnter the number: "))
    second_number=int(input("\nEnter the value of the power: "))
    pwr(first_number,second_number)
elif operation=='6':
    first_number=int(input("\nEnter the number whose squareroot is to be find: "))
    sqrt(first_number)
else:
    print("\n SORRY! Not available in this calculator")

