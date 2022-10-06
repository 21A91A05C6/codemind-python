def roman_to_integer(s):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sum=0
    for i in range(len(s)-1,-1,-1):
        req_num=roman[s[i]]
        if(3*req_num>sum):
            sum=sum+req_num
        else:
            sum=sum-req_num
    return sum
s=input()
print(roman_to_integer(s))