n=int(input())
a=list(map(int,input().split()))
b=len(a)
s=0
for i in range(0,b):
    s=s+a[i]
print(s)