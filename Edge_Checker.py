a,b=map(int,input().split())
if(a>b):
    if(a==10 or b==10):
        res=abs(a-b-10)
    else:
        res=a-b
else:
    #res=b-a
    if(a==10 or b==10):
        res=abs(b-a-10)
    else:
        res=b-a
if(res==1):
    print("Yes")
else:
    print("No")
    