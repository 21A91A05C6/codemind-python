n=int(input())
s=0
avg=0
arr=list(map(int,input().split()))
for i in arr:
    s=s+i
avg=s/n
print("%.2f"%avg)