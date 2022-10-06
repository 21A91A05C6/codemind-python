n=int(input())
s=""
while(n>0):
    n=n-1
    s=chr(n%26+65)+s
    n=n//26
print(s)