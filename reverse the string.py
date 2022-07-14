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

#--------- Reverse the string

st=input()
s=list(st)

l=len(s)

if l%2!=0:
    mid=(int(l/2))   #mid=int(l/2)+1 but due to indexing we do with it (- 1) aand get only l/2
    for i in range(1,mid+1):
        s[mid-i],s[mid+i]=s[mid+i],s[mid-i]
    print("".join(s))
elif l%2==0:
    mid1=int(l/2)-1     #to match indexing do -1
    mid2=mid1+1

    s[mid1],s[mid2]=s[mid2],s[mid1]

    for i in range(1,mid1+1):
        s[mid1-i],s[mid2+i]=s[mid2+i],s[mid1-i]

    print("".join(s))

