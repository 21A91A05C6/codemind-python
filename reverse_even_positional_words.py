s=input()
s=s.split(" ")
for i in s:
    if(s.index(i)%2==0):
        i=i[::-1]
    print(i,end=" ")