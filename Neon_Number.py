n=int(input())
sq=n*n
sum=0
while(sq>0):
    d=sq%10
    sq=sq//10
    sum=sum+d
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")