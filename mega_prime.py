def isprime(n):
    if(n>1):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return 1
n=int(input())
if(isprime(n)==1):
    dc=0
    c=0
    while(n>0):
        d=n%10
        n=n//10
        dc+=1
        if(isprime(d)==1):
            c+=1
    if(dc==c):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
        
        
        
        