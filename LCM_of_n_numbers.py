def lcm(a,b):
    l=max(a,b)
    while(1):
        if l%a==0 and l%b==0:
            break
        else:
            l+=1
    return l
a=int(input())
arr=list(map(int,input().split()))
l=lcm(arr[0],arr[1])
for i in range(2,a):
    l=lcm(l,arr[i])
print(l)