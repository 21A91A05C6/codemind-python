n=int(input())
arr=list(map(int,input().split()))
arr=set(arr)
if(len(arr)<3):
    print(max(arr))
else:
    m=max(arr)
    arr.remove(m)
    m1=max(arr)
    arr.remove(m1)
    print(max(arr))