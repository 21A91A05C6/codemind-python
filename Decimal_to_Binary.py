def dec_to_bin(n):
    if(n>1):
        dec_to_bin(n//2)
    print(n%2,end="")
t=int(input())
while(t>0):
    n=int(input())
    dec_to_bin(n)
    print()
    t-=1