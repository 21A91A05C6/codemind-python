n=int(input())
arr=list(map(int,input().split()))
k=int(input())
m=max(arr)
for i in arr:
    if(m-i<=k):
        print("True",end=" ")
    else:
        print("False",end=" ")
        