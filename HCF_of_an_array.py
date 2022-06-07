n=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    hcf=arr[0]
    j=1
    while(j<n):
        if(arr[j]%hcf==0):
            j+=1
        else:
            hcf=arr[j]%hcf
            i+=1
print(hcf)