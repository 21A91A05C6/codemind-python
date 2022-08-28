def max_col(mat, rows, cols):
    for i in range(cols):
        maxm = mat[0][i]
        for j in range(rows):
            if mat[j][i] > maxm:
                maxm = mat[j][i]
        print(maxm)
n,m=map(int,input().split())
mat=[list(map(int,input().split()))
for i in range(n)]
max_col(mat, n, m);