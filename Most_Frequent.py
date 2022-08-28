n=int(input())
arr=list(map(int,input().split()))
a=set(arr)
l=[]
k=[]
for i in a:
    l.append(arr.count(i))
m=max(l)
for i in l:
    if(l.count(m)==1):
        for i in arr:
            if(arr.count(i)==m):
                req=i
        #break
    else:
        for i in arr:
            if(arr.count(i)==m):
                k.append(i)
                req=min(k)
       # print(min(k))
    #break
print(req)
    