#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     14-07-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n=int(input("Enter the number of natural numbers whose sum of cubes is to be found:  "))

s=0
for i in range(1,n+1):
    s=s+((i**2)*i)
print("The sum of cubes of the first {} natural numbers is = {}".format(n,s))
