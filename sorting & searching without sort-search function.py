#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NC
#
# Created:     08-07-2022
# Copyright:   (c) NC 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#********** search and sort without the in-built functions **********

def sorting(lst):
    l1=len(lst)
    for i in range(l1):
        for j in range(i+1,l1):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    print(lst)
    return lst

def searching(lst):
    s=float(input("enter the number to be searched: "))
    for i in lst:
        if s==i:
            print("The number {} is at index {} in the list.".format(i,lst.index(i)))



#n=int(input("Enter the number of elements you want in the list: "))
#list1=[]

#for i in range(n):
#   x=int(input("Enter the number: "))
#  list1.append(x)

list1= list(map(float, input("Enter the numbers with space: ").split()))

print("The list you created is : \n",list1)

print("\nWhat actions do you want to perform on the list ?\n 1. Sort\n 2.Search")

choice=int(input())

if choice==1:
    sorting(list1)
elif choice==2:
    searching(list1)
else:
    print("Not Available!")







