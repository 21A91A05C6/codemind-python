n=int(input())
sum=0
prod=1
while(n>0):
    d=n%10
    n=n//10
    sum=sum+d
    prod=prod*d
if(sum==prod):
    print("Spy Number")
else:
    print("Not Spy Number")