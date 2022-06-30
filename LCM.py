a,b=map(int,input().split())
n=a*b
for i in range(a,n+1):
    if i%a==0 and i%b==0:
        print(i)
        break