a = list(input())
q = []
ans = 0

for i in range(len(a)):
    if a[i] == '(':
        q.append('(')
    else:  # ')'
        q.pop()
        if a[i - 1] == '(':  # 레이저
            ans += len(q)
        else:  # 쇠막대기의 끝
            ans += 1

print(ans)

#앞에 있던게 (면 그냥 더해주면 되고,
# 만약에 )이 들어왔는데 바로 앞에 있던 게 (라면 레이저이다.
# 그러므로 현재 스택에 있는 len을 더해주면 된다.
# 그리고 앞에 있던 게 )라면 쇠막대기의 끝이다.
# 쇠막대기의 끝마다 1개씩 더해주면 된다.