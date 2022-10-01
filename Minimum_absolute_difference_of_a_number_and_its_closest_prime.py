def isPrime(N):
    for i in range(2, N):
        if (N % i == 0):
            return False
    else:
        
        return True

def getDifference(N):
    if (N == 0):
        return 0
    elif (N == 1):
        return 1
    elif (isPrime(N)):
        return 0

    aboveN = 0
    belowN = 0

    n1 = N + 1
    while (True):
        if (isPrime(n1)):
            aboveN = n1
            break
             
        else:
            n1 += 1

    n1 = N - 1
    while (True):
        if (isPrime(n1)):
            belowN = n1
            break
             
        else:
            n1 -= 1
 
    diff1 = aboveN - N
    diff2 = N - belowN
 
    return min(diff1, diff2)

N = int(input())
print(getDifference(N))