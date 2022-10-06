t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]==arr[k]):
                    c+=1
    if(c==0):
        print("-1")
    else:
        print(c)