n=int(input())
a=list(map(int,input().split()))
a=list(a)
a=set(a)
c=0
for i in a:
    if i%2:
        c+=1
print(c)