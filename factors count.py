import math as m
def factcount(num):
    d=int(m.sqrt(num))
    fc=2
    for i in range(2,d+1):
        if num%i==0:
            if i==num//i:
                fc+=1
            else:
                fc+=2
    return fc
num=int(input())
print(factcount(num))
