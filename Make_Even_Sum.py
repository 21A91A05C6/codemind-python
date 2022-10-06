def findCount(arr, n):
 
    count = 0
 
    for i in range(0, n):
        if (arr[i] % 2 == 1):
             
            # counts only odd
            # numbers
            count += -1
             
    # if the counter is
    # even return 0
    # otherwise return 1
    if (count % 2 == 0):
        return 1
    else:
        return 0
 
# Driver Code
n=int(input())
arr=list(map(int,input().split()))
print(findCount(arr, n))
 
# This code is contributed by
# Smitha Dinesh Semwal