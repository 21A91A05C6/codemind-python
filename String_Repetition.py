s=input()
n=int(input())
ac=0
count=0
for i in s:
    if i=='a':
        ac+=1
l=len(s)
b=n//l*ac
r=n%l
for i in range(r):
    if s[i]=='a':
        count+=1
print(b+count)
