s=input()
c=0
c1=0
c2=0
c3=0
c4=0
for i in s:
    if(i=='b'):
        c=s.count(i)
    if(i=='a'):
        c1=s.count(i)
    if(i=='l'):
        c2=s.count(i)//2
    if(i=='o'):
        c3=s.count(i)//2
    if(i=='n'):
        c4=s.count(i)
print(min(c,c1,c2,c3,c4))