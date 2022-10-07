n=int(input())
k=n
r=0
c=0
while n:
    n=n//10
    c+=1
n=k
while n:
    d=n%10
    r+=d**c
    n=n//10
    c-=1
if r==k:
    print(True)
else:
    print(False)