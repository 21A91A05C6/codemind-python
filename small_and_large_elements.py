s=input()
s=s.split(" ")
for i in s:
    print(min(i),end=" ")
    break
s=s[::-1]
for i in s:
    print(max(i))
    break