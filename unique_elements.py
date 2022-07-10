n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in arr:
    if i not in k:
        k.append(i)
print(*k)
