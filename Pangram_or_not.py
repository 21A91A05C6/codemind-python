def pangram(s):
    s=s.lower()
    alphabets="abcdefghijklmnopqrstuvwxyz"
    for i in alphabets:
        if i not in s:
            return False
    return True
s=input()
print(pangram(s))