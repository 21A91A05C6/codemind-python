def ispallindrome(n):
    temp=n
    rev=0
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    if(temp==rev):
        return 1
    else:
        return 0
def pallindrome(n):
    rev=0
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
x=int(input())
while(1):
    x=x+pallindrome(x)
    if(x==pallindrome(x)):
        print(x)
        break
    else:
        continue