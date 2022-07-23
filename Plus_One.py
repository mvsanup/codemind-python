
n=int(input())
a=list(map(int,input().split()))
s=0
n=n-1
for i in a:
    s=s+i*(10**n)
    n-=1
s=s+1
s=str(s)
b=[]
for i in s:
    b.append(i)
print(*b)

