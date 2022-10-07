def pal(n):
    r=0
    temp=n
    while n:
        d=n%10
        r=r*10+d
        n=n//10
    if r==temp:
        return True
    else:
        return False
n=int(input())
for i in range(n-1,0,-1):
    if pal(i):
        v=i
        break
i=n+1
while True:
    if pal(i):
        d=i
        break
    i+=1
if n-v==d-n:
    print(v,d)
elif n-v>d-n:
    print(d)
elif n-v<d-n:
    print(v)