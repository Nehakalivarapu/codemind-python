n=int(input())
c=0
for i in range(1,n//2):
    if n==i**2:
        c=1
if c==1:
    print('True')
else:
    print('False')