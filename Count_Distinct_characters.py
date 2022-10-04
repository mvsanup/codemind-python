a=str(input())
a=a.lower()
a=list(set(a))
if ' ' in a:
    a.remove(' ')
print(len(a))