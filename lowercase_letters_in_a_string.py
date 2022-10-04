a=str(input())
c=0
for i in a:
    x=ord(i)
    if x>=97 and x<=122:
        c+=1
print(c)