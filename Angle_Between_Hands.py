s=input()
h=int(s[:2])
m=int(s[3:])

a=abs(h*30-(11*m)/2)
if(a<360-a):
    if(a>int(a)):
        print("%.1f"%a)
    else:
        print(a)
else:
    if(360-a>(int)(360-a)):
        print("%.1f"%(360-a))
    else:
        print(360-a)