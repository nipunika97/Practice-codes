#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     16-07-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

d=int(input("Enter the decimal number :  "))
c=[]
while(d>=1):
    q=d%2
    c.append(q)
    d=int(d/2)
c.reverse()
res=int("".join(map(str,c)))
print("The binary of the decimal number {} is : {}".format(res,d))
