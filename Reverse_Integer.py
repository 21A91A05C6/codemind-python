n=int(input())
rev=0
if(n>0):
    
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
else:
    n=abs(n)
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    rev=-rev
print(rev)