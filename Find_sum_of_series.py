x=int(input())
s=0
for i in range(1,x+1):
  s=s+(1/i)
print('{:.2f}'.format(s))