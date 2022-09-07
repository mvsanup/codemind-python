n=input()
n=n.split()
c=0
for i in n:
    if len(i)>c:
        c=len(i)
print(c)
        