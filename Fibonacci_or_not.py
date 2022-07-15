n=int(input())
a=0
b=1
c=0
while(c<n):
    c=a+b
    a=b
    b=c
if c==n:
    print("True")
else:
    print("False")