t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=sorted(arr)
    if(a==arr):
        print("0")
    else:
        print(max(arr)-min(arr))