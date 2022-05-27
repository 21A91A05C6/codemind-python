s1=input()
s2=input()

s1=s1.lower()
s2=s2.lower()

s1=s1.split()
s2=s2.split()

print(len(list(set(s1)&set(s2))))