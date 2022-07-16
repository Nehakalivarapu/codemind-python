a=input()
b=input()
c=a+b
l=[]
for i in c:
    l.append(ord(i))
l=sorted(l)
for i in l:
    print(chr(i),end='')