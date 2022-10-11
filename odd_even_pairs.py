n=int(input())
arr=list(map(int,input().split()))
l=[]
k=[]
for i in arr:
    if i%2!=0:
        l.append(i)
    else:
        k.append(i)
i=0
j=0
while(j<len(l) or i<len(k)):
    if j<len(l):
        print(l[i],end=" ")
    j+=1
    if(i<len(k)):
        print(k[i],end=" ")
    i+=1
if n%2!=0:
    print("0")