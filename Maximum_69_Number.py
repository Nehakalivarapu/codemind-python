a=int(input())
k=a
b=[]
while k:
    d=k%10
    b.append(d)
    k//=10
b=b[::-1]
for i in range(len(b)):
    if b[i]==6:
        b[i]=9
        break
r=0
for i in range(len(b)):
    r=r*10+b[i]
print(r)
