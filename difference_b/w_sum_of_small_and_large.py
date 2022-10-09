l=list(map(str,input().split()))
sum1=0
sum2=0
w=0
for i in l:
    k=ord(min(i))
    p=ord(max(i))
    sum1=sum1+k
    sum2=sum2+p
w=abs(sum2-sum1)
print(w,end=" ")