#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     11-07-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
print("Enter the numbers in the list: \n")
l=list(map(int,input().rstrip().split()))
print(l)

c19=0
c5=0

for i in l:
    if i==19:
        c19+=1
    elif i==5:
        c5+=1
if c19==2 and c5>=3:
    print("There are exactly two 19s and (atleast) three 5s in the list. ")