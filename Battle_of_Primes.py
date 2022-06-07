def prime(s):
    c=0
    for i in range(1,10):
        s1=s+i
        c=0
        for j in range(2,s1):
            if(s1%j==0):
                c+=1
        if(c==0):
            k=i
            break
    return k
a=int(input())
b=int(input())
s=a+b
print(prime(s))