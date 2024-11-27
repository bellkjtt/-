import sys
input = sys.stdin.readline


N, P = map(int, input().split())
stacks = [[0] for _ in range(7)]

cnt = 0
for _ in range(N):
    i, p = map(int, input().split())
    stack = stacks[i]
    while stack[-1] > p:
        stack.pop()
        cnt += 1
    if stack[-1] < p:
        stack.append(p)
        cnt += 1

print(cnt)

#기타줄은 1번부터 6번까지 없다는 점을 들어 리스트를 만든다.
#해당 기타줄의 전 번호가 다음 기타줄보다 크다면 스택에서 팝하고 +1
#아니라면 스택에 더해주고 +1 해준다.
    