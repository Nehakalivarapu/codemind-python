n=int(input())
c=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
max=0
for i in range(n):
    if c[i]<a or c[i]>b:
        k=1
        if max<c[i]:
            max=c[i]
if k==0:
    print('-1')
else:
    print(max)