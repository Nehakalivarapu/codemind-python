n=int(input())
k=n
r=0
while k:
    d=k%10
    r=r*10+d
    k=k//10
b=r+n
r2=0
while b!=r2:
    m=b
    r2=0
    while m:
        d=m%10
        r2=r2*10+d
        m=m//10
    if(r2!=b):
        b=b+r2
print(r2)