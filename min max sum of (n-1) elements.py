#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     10-07-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def miniMaxSum(arr):
    # Write your code here
    lst=[]
    s=sum(i for i in arr)
    for i in arr:
        si=s-i
        lst.append(si)
    print("The sum of {} out of the given {} numbers: \nminimum possible sum = {} \nmaximum possible sum = {}".format((len(arr)-1),len(arr),min(lst),max(lst)))




if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)