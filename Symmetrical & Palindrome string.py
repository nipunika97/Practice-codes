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

def symm(s):
    l=len(s)
    mid=int(l/2)
    flag=0

    for i in range(l):
        if i < mid :
            if s[i]==s[i+mid]:
                flag+=1
    if flag==mid:
        print("The String '{}' is symmetrical".format(s))
    else:
        print("The String '{}' is NOT symmetrical".format(s))



def palin(s):
    l=len(s)
    mid=int(l/2)

    flag=0
    k=l

    for i in range(l):
        if i<mid:
            if s[i]==s[k-1]:
                flag+=1
                k-=1
    if flag==mid:
        print("The String '{}' is Palindrome".format(s))
    else:
        print("The String '{}' is NOT Palindrome".format(s))

string1=input("Enter the String : ")

symm(string1)
palin(string1)
