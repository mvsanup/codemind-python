
t=int(input())
while t:
    a=int(input())
    temp=a
    while True:
        for j in range(2,int(a**0.5)+1):
            if(a%j==0):
                break
        else:
            d=a
            break
        a+=1
    a=temp
    while a:
        for j in range(2,int(a**0.5)+1):
            if(a%j==0):
                break
        else:
            v=a
            break
        a-=1
    a=temp
    if(abs(d-a)<abs(v-a)):
        print(d)
    elif(abs(d-a)>abs(v-a)):
        print(v)
    else:
        print(v)
    t-=1
