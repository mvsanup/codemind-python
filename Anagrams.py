a=str(input())
b=str(input())
a=a.lower()
b=b.lower()
a=list(a)
b=list(b)
a.sort()
b.sort()
if a==b:
    print("True")
else:
    print("False")