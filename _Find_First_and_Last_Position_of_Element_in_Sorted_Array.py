n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,n):
    if(arr[i]==k):
        print(i,end=" ")
        break
for i in range(n-1,-1,-1):
    if(arr[i]==k):
        c+=1
        print(i,end=" ")
        break

if(c==0):
    print("-1 -1")