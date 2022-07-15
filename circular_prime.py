def isprime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return 1
n=int(input())
rev=0
if(isprime(n)==1):
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    if isprime(rev)==1:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")