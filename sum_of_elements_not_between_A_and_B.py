n=int(input())
arr=list(map(int,input().split()))
k,l=map(int,input().split())
sum=0
for i in arr:
    if i<k or i>l:
        #c+=1
        sum=sum+i
print(sum)
'''if(c==0):
    print("-1")'''