a=int(input())
for i in range(a):
    b=int(input())
    n=b
    rev=0
    while(b):
        d=b%10
        rev=rev*10+d
        b=b//10
    if rev==n:
        print('True')
    else:
        print('False')