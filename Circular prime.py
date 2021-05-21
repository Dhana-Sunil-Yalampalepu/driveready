import math as m
def factcount(num,a):
    if a==1:
        return 2
    if num%a==0:
        if a==num//a:
            return 1+factcount(num,a-1)
        else:
            return 2+factcount(num,a-1)
    else:
        return 0+factcount(num,a-1)

num=int(input())
n=num
a=int(m.sqrt(num))
y=factcount(num,a)==2
rev=0
if y==True:
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
        z=factcount(rev,a)==2
    if z==True:
        print("Circular Prime")
    else:
        print("Not Circular")
else:
    print("Not Prime")
