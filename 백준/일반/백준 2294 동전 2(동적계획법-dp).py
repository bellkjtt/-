https://www.acmicpc.net/submit/2294/74797770

import sys

n,m = sys.stdin.readline().split()
n,m =int(n),int(m)

coin = [int(i.rstrip()) for i in sys.stdin.readlines()]

dp =[10001]*(m)
dp.insert(0,0)
for i in range(n):
    for j in range(coin[i],m+1):
        dp[j] = min(dp[j],dp[j-coin[i]]+1)

if dp[m]==10001:
    print(-1)
else:
    print(dp[m])
    
#코인의 가치의 경우의 수를 구하려면 점화식을 써야 한다