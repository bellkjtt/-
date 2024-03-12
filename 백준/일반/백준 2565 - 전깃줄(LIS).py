https://www.acmicpc.net/problem/2565

import sys

n = int(sys.stdin.readline())

ans = [1] * n 

li =[]
for i in range(n):
  a, b = map(int, input().split())
  li.append([a, b])

li.sort()

# print(li)
for i in range(1, n):
    for j in range(i):
        if li[i][1] > li[j][1]:
            # print(shark[i],shark[j])
            ans[i] = max(ans[i], ans[j] + 1)
    # print(ans)

print(n-max(ans))
