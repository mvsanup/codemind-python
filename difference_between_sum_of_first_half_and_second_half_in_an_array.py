n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(n//2):
    b.append(a[i])
for i in range(n//2,n):
    c.append(a[i])
print(abs(sum(b)-sum(c)))
