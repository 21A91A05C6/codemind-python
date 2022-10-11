n=int(input())
arr=list(map(int,input().split()))
c=0
arr.append(arr[0])
arr.append(arr[1])
for i in range(0,len(arr)-2):
    if arr[i]%2==0 and arr[i+2]%2!=0 or arr[i]%2!=0 and arr[i+2]%2==0:
        c+=1
print(c)