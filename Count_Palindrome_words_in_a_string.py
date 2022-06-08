def checkPalin(k):
    if k.lower() == k.lower()[::-1]:
        return True
def countPalin(s):
    c= 0
    words = s.split(" ")
    for i in words:
        if (checkPalin(i)):
            c += 1
    print (c)
countPalin(input())