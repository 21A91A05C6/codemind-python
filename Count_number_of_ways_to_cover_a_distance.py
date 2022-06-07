def distance(n):
    sum=0
    if(n<0):
        return 0
    elif(n==0):
        return 1
    else:
        sum=distance(n-1)+distance(n-2)+distance(n-3)
        return sum
n=int(input())
print(distance(n))