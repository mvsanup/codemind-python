def fun(n):
    c=0
    if n==0:
        return 1
    if n<0:
        n=-n
    while n:
        c+=1
        n=n//10
    return c
m,n=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if fun(i)==n:
        c+=1
print(c)