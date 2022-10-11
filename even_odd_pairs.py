n=int(input())
arr=list(map(int,input().split()))
l=[]
k=[]
for i in arr:
    if i%2==0:
        l.append(i)
    else:
        k.append(i)
i=0
j=0
while(i<len(l) or j<len(k)):
    if i<len(l):
        print(l[i],end=" ")
    i+=1
    if(j<len(k)):
        print(k[j],end=" ")
    j+=1
if n%2!=0:
    print("0")