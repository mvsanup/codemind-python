def fun(n):
    c=0
    while n:
        e=n%10
        c+=e
        n=n//10
    return c
    
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    c+=fun(i)
print(c)