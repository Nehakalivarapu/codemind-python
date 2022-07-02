n=int(input())
t=n
k=0
while(n>5):
    if(n%2==0):
        n=n//2
    elif(n%3==0):
        n=n//3
    elif(n%5==0):
        n=n//5
    else:
        k=1
        break
if k==0 and t>0:
    print("Ugly Number")
else:
    print("Not Ugly Number")