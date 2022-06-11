def maxprod(arr):
    arr.sort()
    return (arr[-1]-1)*(arr[-2]-1)
arr=list(map(int,input().split()))
print(maxprod(arr))