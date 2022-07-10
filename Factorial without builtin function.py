#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     09-07-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n=int(input("Enter the number whose factorial is to be found: "))

def fact(x):
    p=1
    for i in range(1,x+1):
        p=p*i
    print("The factorial of {} is ={}".format(x,p))

fact(n)
