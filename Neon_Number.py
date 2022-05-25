n=int(input())
sum=0
for i in range(n):
    m=n*n
    d=m%10
    sum=sum+d
    m=m//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")