def isprime(n):
    if(n>1):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return 1
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if isprime(i)==1:
        print(i)