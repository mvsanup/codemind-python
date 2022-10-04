def rev(n):
    s=0
    while n:
        e=n%10
        s=s*10+e
        n=n//10
    return s
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(rev(i))
print(*b)