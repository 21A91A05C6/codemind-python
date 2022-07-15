def isprime(n):
    if n>1:
        
        for i in range(2,n):
            if n%i==0:
                return 0
        else:
            return 1
    else:
        return 0
n=int(input())
a=[]
c=0
for i in range(1,n+1):
    x=0
    if isprime(i)==1:
        if(n%i==0):
            x=1
            k=n//i
            if isprime(k)==1:
                
                print(i,k,end=" ")
                break
            else:
                print("-1")