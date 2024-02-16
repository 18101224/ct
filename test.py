import sys
from collections import defaultdict

n = int(sys.stdin.readline())
result = [[1 for i in range(10)]] #한자리
result[0][0] = 0

result.append(
    [ 2 for i in range(10)] #두자리
)
result[-1][0]=1
result[-1][1] = 1
result[-1][9]=1

for i in range(2,n) :
    result.append(
        defaultdict(int)
    )
    for i in range(1,9):
        result[-1][i] = result[-2][i-1]+result[-2][i+1]
    result[-1][0] = result[-2][1]
    result[-1][9] = result[-2][8]

if n == 2:
    print(17)
elif n == 1 :
    print(9)
else:
    out = 0
    for i,v in result[-1].items():
        out+=v
    print(out%1000000000)