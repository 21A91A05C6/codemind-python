t = int(input())
while(t>0):
    n =input()
    a = []
    for i in n:
        a.append(int(i))
    mi = min(a)
    m = max(a)
    c=0
    arr= []
    #print(mi,m,end=" ")
    for i in range(mi,m+1):
        arr.append(i)
    #print(arr)
    if sorted(a)==sorted(arr):
        print('YES')
    else:
        print('NO')
    t-=1