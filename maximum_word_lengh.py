s=input()
a=[]
s=s.split()
for i in range(len(s)):
    a.append(len(s[i]))
print(max(a))