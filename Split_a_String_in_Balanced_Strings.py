def balancedStringSplit(s):
        l = 0
        r = 0
        res = 0
        for i in s:
            if i == 'L':
                l += 1
            elif i == 'R':
                r += 1
            if l == r:
                res += 1
                l = 0
                r = 0
        return res
s=input()
print(balancedStringSplit(s))