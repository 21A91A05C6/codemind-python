t=int(input())
for i in range(t):
    a=int(input())
    for n in range(a,1,-1):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            #print(n,end=" ")
            break
    b=a
    while(1):
        for i in range(2,a):
            if a%i==0:
                break
        else:
                #print(k,end=" ")
            break
        a+=1
    if(abs(b-n)>abs(a-b)):
        print(a)
    else:
        print(n)