octal=int(input())
b=[]
k=""
sum=0
i=0
while(octal>0):
    d=octal%10
    octal=octal//10
    sum=sum+d*pow(8,i)
    i+=1
while(sum>0):
    d=sum%2
    sum=sum//2
    b.append(d)
for i in b:
    k+=str(i)
print(k[::-1])