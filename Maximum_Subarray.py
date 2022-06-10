def maxSubArraySum(arr,size):   
    max = arr[0]
    sum = 0
    
    for i in range(0, size):
        sum = sum + arr[i]
        if sum < 0:
           sum = 0
        
        
        elif (max < sum):
            max = sum
            
    return max
n=int(input())
arr=list(map(int,input().split()))
print(maxSubArraySum(arr,n))