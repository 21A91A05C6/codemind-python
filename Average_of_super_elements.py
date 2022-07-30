n=int(input())
d=list(map(int,input().split()))
c=0
sum=0
k=[]
for i in d:
    if i==d.count(i):
        k.append(i)
k=set(k)
#print(k)
for i in k:
    sum+=i
    c+=1
if(c==0):
    print("-1")
else:
    print("%.2f"%(sum/c))
