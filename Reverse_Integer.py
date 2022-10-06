n=int(input())
r=0
a=n
if n<0:
    n=-n
while n:
    d=n%10
    r=r*10+d
    n=n//10
if a>0:
    print(r)
else:
    print(-r)