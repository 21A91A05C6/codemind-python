n=int(input())
arr=list(map(int,input().split()))
s=0
s1=0
res=0

for i in range(0,n,2):
    s=s+arr[i]
for i in range(n-1,-1,-2):
    s1=s1+arr[i]
res=abs(s-s1)
if(res%4==0 and res!=0):
    print("X")
elif(res==0):
    print("Y")
else:
    print("Y")