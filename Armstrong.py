def armstrong(n):
    t=n
    s=0
    while n:
        r=n%10
        n=n//10
        s=r*r*r+s
    if s==t:
        print("Armstrong")
    else:
        print("Not Armstrong")
n=int(input())
armstrong(n)
