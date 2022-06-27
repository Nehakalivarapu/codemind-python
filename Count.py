n=int(input())
arr=list(map(int,input().split()))
e=0
o=0
for i in range(len(arr)):
    if arr[i]%2==0:
        e+=1
    else:
        o+=1
print(e,o,end=' ')
    