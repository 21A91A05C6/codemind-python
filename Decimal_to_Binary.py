t=int(input())
while(t>0):
    n=int(input())
    n=bin(n)
    n=n.replace("0b","")
    print(n)
    t-=1