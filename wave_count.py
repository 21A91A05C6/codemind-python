n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(1,len(arr)-1,2):
    if arr[i-1]<arr[i]:
        c+=1
    else:
        c=0
        break
if(c==0):
    print("-1")
else:
    print(c)