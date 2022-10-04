def fun(n):
    c=0
    while n:
        c+=1
        n=n//10
    return c
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(fun(i))
c=min(b)
e=0
for i in a:
    if fun(i)==c:
        e+=1
print(e)