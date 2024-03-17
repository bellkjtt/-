#사탕을 회전해서 뽑을 때 몇 번 회전하는지에 대한 최소값을 구하는 문제
#입력은 어떤 사탕을 뽑을지가 주어지며, 무조건 첫번째 값만 뽑을 수 있다.
#deque를 사용하여 왼쪽, 오른쪽을 세서 뽑는다.

import sys
from collections import deque

n,_ = map(int,sys.stdin.readline().split())
want = list(map(int, sys.stdin.readline().split()))
candy = deque([i for i in range(1,n+1)])
# print(want)

def turn(candy,want):
    cnt_left=0
    cnt_right=0
    temp=deque(list(candy))
    while candy[0]!=want:
        cnt_left+=1
        left=candy.appendleft(candy.pop())
        # print(candy,'오른쪽으로')

    while temp[0]!=want:
        cnt_right+=1
        right=temp.append(temp.popleft())
        # print(temp,'왼쪽으로')
    
    return min(cnt_left,cnt_right)

ans=0
for j in want:
    # print(candy,'시작')
    turn_val =turn(candy,j)
    ans+=turn_val
    candy.popleft()
    # print(candy,'끝')
    
print(ans)
