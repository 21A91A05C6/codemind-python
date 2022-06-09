def maximum69Number ( num):
        s=str(num)
        l=list(s)
        for i in range(len(s)):
            if l[i]=="6":
                l[i]="9"
                break
        s=''.join(l)
        return int(s)
n=int(input())
print(maximum69Number (n))