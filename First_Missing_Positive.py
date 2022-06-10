def firstMissingPositive(nums):
        i = 1
        nums = set(nums)
        while i in nums : 
            i += 1 
            #print(i,end=" ")
    
        return i 
n=int(input())
arr=list(map(int,input().split()))
print(firstMissingPositive(arr))