from collections import deque
import sys

n = int(sys.stdin.readline())

# print(deque)

sq = [int(i) for i in sys.stdin.readline().split()]
# print(sq)
li = [deque([int(i)]) for i in sys.stdin.readline().split()]
# print(li)
m = int(sys.stdin.readline())
c = [int(i) for i in sys.stdin.readline().split()]
# print(m,c)
import sys
from collections import deque
input = sys.stdin.readline

## 스택은 무시하고 큐만 deque에 추가하기
queue = deque([])
for i in range(n):
  if sq[i] == 0:
    queue.appendleft(li[i][0])
else:
  if queue == []:
    print(*c)
    sys.exit()

## deque가 하나의 큐 처럼 작동
for i in range(m):
  queue.append(c[i])
  print(queue.popleft(), end = " ")
# print(' '.join(map(str,ans)))
    