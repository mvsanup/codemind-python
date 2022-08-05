
n=int(input())
l=list(map(int,input().split()))
a,b=0,0
for i in l:
    if i%2:
        a+=i
    else:
        b+=i
print(abs(a-b))
