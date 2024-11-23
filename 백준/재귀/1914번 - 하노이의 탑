n = int(input())

def move(N, start, to):
    print(start,to)

def hanoi(N, start, to, via):
    if N==1:
        move(N,start,to)
    else:
        hanoi(N-1,start,via,to)
        move(N,start,to)
        hanoi(N-1,via,to,start)

if n<=20:
    print(2**(n)-1)
    hanoi(n,1,3,2)
else:
    print(2**(n)-1)
    

#재귀의 특성상 점화식이다.
#가장 마지막에 불러오는 Base case가 결국 1번에서 3번으로 옮기는 것.
#그리고 나머지는 N-1에서 1번에 있는 것들을 2번으로 옮기고,
#맨 밑의 원판을 옮긴 후,
#다시 2번에서 3번으로 전부 옮긴다.
#그런 방식으로 20 이하는 경로를 표시하고, 20 이상은 표시하지 않는다.