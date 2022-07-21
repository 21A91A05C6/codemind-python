def isprime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return 1
n=int(input())
i=1
if isprime(n)==1:
    print("0")
else:
    
    while(i<=100):
        if(isprime(n+i)==1):
            a=n+i
            #break
            #print(a)
            break
        i+=1
    j=1
    while(j<=100):
        if(isprime(n-j)==1):
            b=n-j
            #print(b)
            break
        j+=1
    if((min(abs(n-b),abs(a-n)))==abs(n-b)):
        print(abs(n-b))
    else:
        print(abs(n-a))
