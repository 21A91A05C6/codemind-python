def longestVowel(s):
    c=0
    count=0
    for i in s:
        if i in "aeiouAEIOU":
            c+= 1
            
        else:
            count= max(count,c)
            c=0
    return max(count,c)
 
# Driver code

s =input()
print (longestVowel(s))