n=int(input())
a=list(map(int,input().split()))
b=[]
c=1
for i in a:
    c=i*i
    b.append(c)
b=sorted(b)
print(*b)
    