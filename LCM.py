n,m=map(int,input().split())
k=max(n,m)
while(1):
    if(k%n==0 and k%m==0):
        lcm=k
        break
    k+=1
print(lcm)
    