n=int(input())
a=n%10
while(n):
    r1=n%10
    if r1>a:
        a=r1
    n=n//10
print(a)