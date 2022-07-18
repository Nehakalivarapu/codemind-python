n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]==0:
        a.remove(a[i])
        a.append(0)
print(*a)