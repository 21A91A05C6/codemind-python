n=int(input())
arr=list(map(int,input().split()))
c=0
oc=0
for i in arr:
    if i%2!=0:
        c+=1
for i in range(len(arr)):
    if(arr[i]%2!=0 and i%2!=0):
        oc+=1
if(c==oc):
    print("True")
else:
    print("False")