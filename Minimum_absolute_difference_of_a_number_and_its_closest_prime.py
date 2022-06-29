def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
for j in range(a,2,-1):
    if prime(j):
        n=j
        break
for p in range(a,a+100):
    if prime(p):
        m=p
        break
if abs(n-a)<=abs(m-a):
    print(abs(n-a))
else:
    print(abs(m-a))