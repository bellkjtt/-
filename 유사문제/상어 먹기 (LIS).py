import sys

n = int(sys.stdin.readline())
shark = [int(i.rstrip()) for i in sys.stdin.readline().split()]

ans = [1] * n 

# print(shark)
for i in range(1, n):
    for j in range(i):
        if shark[i] > shark[j]:
            # print(shark[i],shark[j])
            ans[i] = max(ans[i], ans[j] + 1)
    # print(ans)

print(max(ans))

#최장 부분 증가 수열을 구하는 문제