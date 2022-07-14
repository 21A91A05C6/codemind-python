n=int(input())
m=int(input())
c=0
dc=0
for k in range(n,m+1):
    dc=0
    c=0
    temp=k
    while(k>0):
        d=k%10
        k=k//10
        dc+=1
        if(d==0):
            break
        else:
            
            if(temp%d==0):
                c+=1
    if(dc==c):
        print(temp,end=" ")