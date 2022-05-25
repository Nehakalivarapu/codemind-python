n=int(input())
z=0
while(n!=0):
    d=n%10
    n=n//10
    if(d>z):
        z=d
print(z)