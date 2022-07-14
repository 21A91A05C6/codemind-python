n=int(input())
sum=0
s=0
for i in range(1,n):
    if n%i==0:
        #print(i)
        s+=i
if n==s:
    print("True")
else:
    print("False")
