import sys
input = sys.stdin.readline

a = int(input())
b = [list(map(int,input().split())) for _ in range(a)]
b.sort(key=lambda x: (x[1],x[0])) #두번째 후 첫번째 정렬
[print(b[i][0],b[i][1]) for i in range(a)] #출력


# 더 빠른 코드
import sys

def cond(dot):
    x, y = dot.split()
    return int(y) + int(x)/1000000

dots = sorted(sys.stdin.readlines()[1:], key=lambda x: cond(x))
print(''.join(dots))

#readlines로 불러오면 바로 출력된다.
