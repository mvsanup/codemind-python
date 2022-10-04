a=str(input())
v="aeiou"
a=a.lower()
c=0
for i in a:
    if i in v:
        c+=1
print(c)