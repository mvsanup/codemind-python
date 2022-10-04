def pal(n):
    s=0
    while n:
        e=n%10
        s=s*10+e
        n=n//10
    return s
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if pal(i)==i:
        c+=1
print(c)