
n=int(input())
a=0
while n:
    d=n%10
    n=n//10
    a+=d*d
    if n==0 and a>9:
        n=a
        a=0
if a==1 or a==7:
    print("True")
else:
    print("False")
