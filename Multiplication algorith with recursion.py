def something(a,b):
    d=0
    if  a%2==1:
        d=d+b
        if a==3:
            b=b*2
            d=d+b
            return d
        else:
            return d
    #print(a,b)
    return something(a//2,b*2)
a,b=map(int,input().split())
print(something(a,b))
