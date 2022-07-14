def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if isprime(i)==0:
            c+=1
print(c+1)