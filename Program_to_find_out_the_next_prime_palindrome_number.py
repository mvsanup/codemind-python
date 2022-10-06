def pri(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
def pal(n):
    k=n
    r=0
    while n:
        d=n%10
        r=r*10+d
        n=n//10
    if r==k:
        return 1
    else:
        return 0
n=int(input())
n=n+1
while True:
    if pri(n) and pal(n):
        print(n)
        break
    n+=1     
        
                