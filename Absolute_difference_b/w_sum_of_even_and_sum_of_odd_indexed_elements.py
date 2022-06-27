n=int(input())
a=list(map(int,input().split()))
b=len(a)
s=0
s1=0
for i in range(0,b):
    if (i%2==0):
        s=s+a[i]
    if(i%2!=0):
        s1=s1+a[i]
print(abs(s1-s))