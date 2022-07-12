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


#Write a Python program to find the strings in a given list, starting with a given prefix.

def teststr(st,pre):
    return[s for s in st if s.startswith(pre)]

st=list(map(str,input("Enter the words:\n").rstrip().split()))
pre=str(input("Enter the prefix:  "))
l=list([pre,st])

print(teststr(st,pre))