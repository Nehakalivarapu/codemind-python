n=int(input())
z=0
temp=n
while(n):
    d=n%10
    n=n//10
    z=z*10+d
if(temp==z):
    print("True")
else:
    print("False")