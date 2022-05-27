def anagram(s,s1):
    s=s.lower()
    s1=s1.lower()
    for i in s:
        if i not in s1:
            return False
    return True
s=input()
s1=input()
print(anagram(s,s1))