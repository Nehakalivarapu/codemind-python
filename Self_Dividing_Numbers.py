n=int(input())
m=int(input())
c=0
c1=0
for i in range(n,m+1):
    a=i
    c=0
    c1=0
    while a:
        d=a%10
        a=a//10
        c+=1
        if d==0:
            continue
        if i%d==0:
            c1+=1
    if c==c1:
        print(i,end=' ')
        