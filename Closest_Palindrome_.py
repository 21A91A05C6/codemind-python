def ispallindrome(n):
    temp=n
    rev=0
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    if(rev==temp):
        return 1
n=int(input())
i=1
a=0
b=0
while(i<=10):
    if(ispallindrome(n+i)==1):
        a=n+i
        break
        #print(a)
    i+=1
j=1
while(j<=10):
    if(ispallindrome(n-j)==1):
        b=n-j
        #print(b)
        break
    j+=1
#print(n,a,b,end=" ")
if(abs(n-b)==abs(a-n)):
    print(b,a,end=" ")
elif(abs(n-b)<=abs(a-n)):
    print(b)
else:
    print(a)