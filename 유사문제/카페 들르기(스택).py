#카페에 몇 명이나 들르는지를 세는 문제.
#입력은 10:00:00 23:59:59 와 같이 입장 시간과 퇴장 시간
# date time을 이용해서 한 뒤, 스택을 쌓아가며 겹치지 않는 구간을 센다.
# 퇴장시간이 같을 수 있다는 걸 고려.

import sys
from datetime import datetime
from collections import deque

n,m = map(int,sys.stdin.readline().split())
log ={}
for _ in range(m):
    start, left = sys.stdin.readline().split()
    start_time = datetime.strptime(start, "%H:%M:%S").time()
    left_time = datetime.strptime(left, "%H:%M:%S").time()
    start_seconds = (start_time.hour * 3600) + (start_time.minute * 60) + (start_time.second)
    left_seconds = (left_time.hour * 3600) + (left_time.minute * 60) + (left_time.second)
    log[start_seconds]= left_seconds

log = dict(sorted(log.items()))
print(log)
cnt=0
stack=[]
for i,j in log.items():
    print(stack,'시작스택')
    if cnt<n:
        cnt+=1
        stack.append(i)
    else:
        for k in stack:
            print(log[k],i)
            if log[k]<=i and (i not in stack):
                stack.pop(stack.index(k))
                stack.append(i)
                cnt+=1
        print(stack)
print(cnt)
