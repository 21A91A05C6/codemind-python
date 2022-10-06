n=int(input())
s=input()
sum=0
for i in range(0,len(s)-1):
    sum=sum+abs(int(s[i+1])-int(s[i]))
d=n-sum-1
if((d%3)==0):
    print('Sudhir')
else:
    print('Ashok')