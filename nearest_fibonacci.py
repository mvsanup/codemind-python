
n=int(input())
a=0
b=1
arr=[]
arr.append(a)
arr.append(b)
i=0
while i<15:
    c=a+b
    arr.append(c)
    a=b
    b=c
    i+=1
arr.append(n)
arr.sort()
for i in range(len(arr)):
    if arr[i]==n:
        if abs(arr[i-1]-arr[i])>abs(arr[i]-arr[i+1]):
            print(arr[i+1])
        elif abs(arr[i-1]-arr[i])==abs(arr[i]-arr[i+1]):
            print(arr[i-1],arr[i+1])
        else:
            print(arr[i-1])
            
