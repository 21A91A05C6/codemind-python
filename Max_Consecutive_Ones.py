def MaxOnes(nums):
    c= 0
    m= 0
    for i in range(len(nums)):
        if nums[i]==1:
            c+=1
        else:
            if c>m:
                m = c
            c= 0
    if c>m:
        m = c
    return m
n=int(input())
arr=list(map(int,input().split()))
print(MaxOnes(arr))