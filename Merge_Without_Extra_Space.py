t=int(input())
a=[]
b=[]

while(t>0):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(a)+list(b)
    c=sorted(c)
    print(*c)
    t-=1