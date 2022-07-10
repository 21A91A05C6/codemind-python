n=int(input())
arr=list(map(int,input().split()))
k=[]
c=0
for i in arr:
    if i==arr.count(i):
        #print(i)
        c+=1
        k.append(i)
print(len(set(k)))
