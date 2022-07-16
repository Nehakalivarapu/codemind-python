t=int(input())
for i in range(t):
    n=input()
    r=0
    d=n[::-1]
    if(n==d):
        e=len(n)
        if(e%2==0):
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')
        