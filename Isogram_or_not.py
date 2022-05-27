def isogram(s):
    l=len(s)
    b=len(set(s))
    if(l==b):
        return True
    else:
        return False
s=input()
print(isogram(s))