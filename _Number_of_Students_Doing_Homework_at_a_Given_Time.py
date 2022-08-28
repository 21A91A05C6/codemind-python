st=int(input())
sta=list(map(int,input().split()))
et=int(input())
end=list(map(int,input().split()))
qt=int(input())
c=0
for i in range(st):
    if(sta[i]<=qt<=end[i]):
        c+=1
print(c)