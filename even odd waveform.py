num=int(input())
d=0
while num:
    r=num%10
    num=num//10
    d=num%10
    if abs(r-d)%2==0:
        print("Not Waveform")
        break
else:
    print("Waveform")
    
