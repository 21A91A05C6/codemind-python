n=int(input())
arr=list(map(int,input().split()))
min=9999
for i in range(0,len(arr)):
    if(min>arr[i]):
        min=arr[i]
for i in range(min,0,-1):
    flag=0
    for j in range(0,n):
        if(arr[j]%i!=0):
            flag=1
            break
    if(flag==0):
        print(i)
        break