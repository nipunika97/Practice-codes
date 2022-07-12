#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     12-07-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

st1=input("Enter the time in 12-hour format:\n")

def convertt(st):
    if st[-2:]=="AM" and st[:2]=="12":
        return "00"+st[2:-2]
    elif st[-2:]=="AM":
        return st[:-2]
    elif st[-2:]=="PM" and st[:2]=="12":
        return st[:-2]
    else:
        return (str(int(st[:2])+12) + st[2:-2])


print("The time in 24-hour format is: ",convertt(st1))