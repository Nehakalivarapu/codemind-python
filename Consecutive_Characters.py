a=input()
ma=c=0
for i in range(len(a)):
    t=a[i]
    c=0
    for j in range(i,len(a)):
        if a[j]==a[i] and a[j-1]==a[i] and i>0:
            c+=1
            if ma<c:
                ma=c
        else:
            break
print(ma+1)