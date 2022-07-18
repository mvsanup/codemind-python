n=int(input())
a=list(map(int,input().split()))
n=n-1
s=0
for i in a:
    if i==1:
        s+=(2**n)
    n=n-1
print(s)