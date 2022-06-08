def unique(s):
     frequency = {}
     for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] +=1
     for i in range(len(s)):
        if frequency[s[i]] == 1:
            return s[i]
     return -1
print(unique(input()))