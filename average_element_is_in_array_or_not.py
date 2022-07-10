n=int(input())
arr=list(map(int,input().split()))
sum=0
avg=0
for i in arr:
    sum=sum+i
avg=sum//n
for i in arr:
    if i==avg:
        print("True")
        break
else:
    print("False")
