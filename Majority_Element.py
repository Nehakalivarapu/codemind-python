n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    c=a.count(i)
    b.append(c)
k=max(b)
f=b.index(k)
print(a[f])

