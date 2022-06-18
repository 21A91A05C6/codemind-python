t=int(input())
while(t>0):
    binary=int(input())
    octal = 0
    decimal = 0
    i = 0
    while (binary>0):
          d=binary%10
          binary=binary//10
          decimal = decimal +d* pow (2, i)
          i+=1
    i = 1
    while (decimal != 0):
          octal = octal + (decimal % 8) * i
          decimal = decimal // 8
          i = i * 10
    print(octal)
    t-=1