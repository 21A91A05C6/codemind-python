n=int(input())
arr=list(map(int,input().split()))
j=0
sum=0
for i in range(len(arr)-1,-1,-1):
    sum=sum+arr[i]*pow(2,j)
    #print(sum)
    j+=1
print(sum)