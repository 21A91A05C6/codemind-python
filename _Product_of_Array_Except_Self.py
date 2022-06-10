def productExceptSelf(nums,n):
    a=[]
    prod = 1
    for i in range(len(nums)):
        a.append(prod)
        
        prod = prod * nums[i]
        
    prod1 = 1
    for i in range(n-1, -1, -1):
        a[i] = a[i] * prod1
        #print(a[i],end=" ")
        prod1 = prod1 * nums[i]
    return a
    
n=int(input())
arr=list(map(int,input().split()))
print(*productExceptSelf(arr,n))