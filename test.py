import sys

n = int(input())
mab = [[]]
for i in range(n):
    mab.append(list(map(int,sys.stdin.readline().split())))
result = [[1001 for j in range(3)] for i in range(n+1)]
result[1] = mab[1]
for i in range(2,n+1):
    result[i][0] = min(result[i-1][1],result[i-1][2]) + mab[i][0]
    result[i][1] = min(result[i-1][0],result[i-1][2]) + mab[i][1]
    result[i][2] = min(result[i-1][0],result[i-1][1]) + mab[i][2]

print(min(result[-1]))
