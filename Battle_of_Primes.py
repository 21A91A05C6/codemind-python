def prime(s):
    for i in range(1,10):
        s1=s+i
        for j in range(2,s1):
            if(s1%j==0):
                break
        else:
            k=i
            break
    return k
a=int(input())
b=int(input())
s=a+b
print(prime(s))