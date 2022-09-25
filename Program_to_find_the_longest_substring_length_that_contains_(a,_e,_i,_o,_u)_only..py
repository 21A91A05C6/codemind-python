def isvowel(ch):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        return 1
s = input()
c=0
max_=0
for i in s:
    if(isvowel(i)==1):
        c+=1
    else:
        max_=max(c,max_)
        c=0
print(max(max_,c))
        