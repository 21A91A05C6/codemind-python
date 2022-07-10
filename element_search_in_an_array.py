n=int(input())
arr=list(map(int,input().split()))
avg=int(input())
for i in arr:
    if i==avg:
        print("True")
        break
else:
    print("False")
