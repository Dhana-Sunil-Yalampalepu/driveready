n=int(input())
h=input()
j=[]
f=[]
e=[]
#i=n
for i in range(n):
    d=h[i:i+1]
    j.append(d)
    c=ord(j[i])
    f.append(c)
    for g in range(i):
        diff=abs((f[i]-f[g]))
        e.append(diff)
#print(j)
#print(f)
#print(e)
print(min(e))
