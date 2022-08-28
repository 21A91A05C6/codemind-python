n,m=map(int,input().split())
arr=list(map(int,input().split()))
l=[]
for i in range(m,n):
    l.append(arr[i])
for i in range(0,m):
    l.append(arr[i])
for i in l:
    print(i,end=" ")