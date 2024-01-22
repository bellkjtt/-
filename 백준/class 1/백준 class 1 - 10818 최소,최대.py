import sys
_, *A = map(int, sys.stdin.read().split())
print(min(A), max(A))

#최소 최대는 내장함수인 min, max를 활용하는 게 가장 빠르다.
#자세한 사항은 스택오버플로우 참조