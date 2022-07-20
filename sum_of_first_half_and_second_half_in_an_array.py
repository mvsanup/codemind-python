n=int(input())
a=list(map(int,input().split()))
x=[]
y=[]
for i in range(n//2):
    x.append(a[i])
for i in range(n//2,n):
    y.append(a[i])
print(sum(x))
print(sum(y))
    