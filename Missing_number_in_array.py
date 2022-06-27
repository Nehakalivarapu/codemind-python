t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    k=1
    for j in b:
        if j!=k:
            print(j-1)
            break
        k+=1
    if(k>len(a)):
        print(k)