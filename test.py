from collections import Counter
import sys

_ = int(input())
nums = list(map(int, sys.stdin.readline().split()))
count = Counter(nums)
result = [None for i in range(len(nums))]
result[-1] = (-1, -1)
for idx in range(len(nums) - 2, -1, -1):
    if count[nums[idx]] < count[nums[idx + 1]]:
        result[idx] = (idx + 1, count[nums[idx + 1]])
    else:
        idx1 = idx + 1
        while True:
            if result[idx1][1] == -1:
                result[idx] = (idx, -1)
                break
            else:
                if count[nums[result[idx1][0]]] > count[idx]:
                    result[idx] = (result[idx1][0], count[nums[result[idx1][0]]])
                    break
                else:
                    idx1 = result[idx1][0]

for i in result:
    if i[1] == -1:
        print(-1, end=' ')
    else:
        print(nums[i[0]], end=' ')

