t=int(input())
while(t>0):
    n=int(input())
    s=input()
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print("-1")
    t-=1        
            