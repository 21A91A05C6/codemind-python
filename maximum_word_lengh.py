s=input()
s=s.split(" ")
max=0
for i in s:
    m=len(i)
    if(max<m):
        max=m
print(max)