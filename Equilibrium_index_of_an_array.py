for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    s=sum(arr)
    c=res=0
    for i in range(n):
        s=s-arr[i]
        if(res==s):
            print(i)
            c=1
        res+=arr[i]
    if(c==0):
        print(-1)
        