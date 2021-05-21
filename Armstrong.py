def armstrong(n):
    t=u=n
    s=0
    dc=0
    while u:
        u=u//10
        dc+=1
    while n:
        r=n%10
        n=n//10
        s=r**dc+s
    if s==t:
        print("Armstrong")
    else:
        print("Not Armstrong")
n=int(input())
armstrong(n)
