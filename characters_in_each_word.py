n=input()

if ' ' not in n:
    print(len(n))
else:
    n=n.split()
    for i in n:
        print(len(i),end=' ')

