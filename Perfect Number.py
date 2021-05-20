def perfect(n):
    d=0
    rev=n
    for i in range(1,n//2+1):
        if n%i==0:
            d=d+i
    print(d)
    if rev==d:
        print("Perfect")
    else:
        print("Not Perfect")
n=int(input())
perfect(n)
