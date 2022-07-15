n=int(input())
sq=n*n
rev=0
rev1=0
while(n>0):
    d=n%10
    n=n//10
    rev=rev*10+d
sq1=rev*rev
while(sq1>0):
    d=sq1%10
    sq1=sq1//10
    rev1=rev1*10+d
if sq==rev1:
    print("True")
else:
    print("False")