n=int(input())
sq=0
while(sq!=1 and sq!=4):
    sq=0
    while(n>0):
        d=n%10
        n=n//10
        sq=sq+(d*d)
    n=sq
if sq==1 or sq==7:
    print("True")
else:
    print("False")