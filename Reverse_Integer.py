n=int(input())
t=n
rev=0
k=0
if n<0:
    n=n+(n*(-2))
while(n!=0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(t<0):
    k=rev-(rev*2)
    print(k)
else:
    print(rev)