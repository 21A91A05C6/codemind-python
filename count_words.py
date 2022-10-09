s=input().lower().split()
c=0
for i in s:
    #for j in range(len(i)):
    if i[0] in "aeiou" and i[len(i)-1] not in "aeiou":
        c+=1
            
        #print(i[len(i)-1])
    #print()
print(c)