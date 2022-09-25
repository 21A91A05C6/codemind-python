t=int(input())
x=0
for i in range(t):
    s =input()
    if s[0] == '+' or s[1] == '+':
        x+=1
    else:
        x-=1
print (x)
