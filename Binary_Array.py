n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(i!=1 and i!=0):
        #print(i)
        c+=1
if(c==0):
    print("True")
else:
    print("False")
#print(c)
#print(arr)