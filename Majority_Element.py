n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in arr:
    if(arr.count(i)!=0):
        b.append(i)
for i in b:
    if(arr.count(i)>(n//2)):
        print(i)
        break
