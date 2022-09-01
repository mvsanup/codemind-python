def sum(n):
    s=0
    while n:
        d=n%10
        s+=d
        n//=10
    return s
n=int(input())
while True:
    x=str(n)
    if len(x)==1:
        break
    else:
        n=sum(n)
print(n)