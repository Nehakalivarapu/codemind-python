s=input()
b=s.split()
a=[]
for i in range(len(b)):
    k=len(b[i])
    a.append(k)
print(min(a))