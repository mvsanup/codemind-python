n,k,p=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k):
    x=a.pop()
    a.insert(0,x)
for i in range(p):
    b=int(input())
    print(a[b])