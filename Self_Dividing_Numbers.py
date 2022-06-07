def isself(n):
    temp=n
    dc=0
    c=0
    while(n>0):
        d=n%10
        n=n//10
        dc+=1
        if(d==0):
            return 0
        else:
            if(temp%d==0):
                c+=1
    if(dc==c):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(isself(i)):
        print(i,end=" ")