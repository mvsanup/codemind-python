n=int(input())
a=list(map(int,input().split()))
b=[]
c=n//2
for i in range(0,c):
    b.append(a[i])
    b.append(a[i+c])
print(*b)