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
a=int(m.sqrt(num))
print(factcount(num,a))
