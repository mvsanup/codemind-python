n=int(input())
a=list(map(int,input().split()))
b=0
for i in a:
    if i%2:
        b+=i
print(b)