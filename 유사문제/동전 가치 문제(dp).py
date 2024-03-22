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
    
# 예를 들어 가치가 2, 3인 단위의 동전이 있을 때는 
# 가치 15를 만들기 위해 가치 3짜리 동전 5개를 사용하는 것이 동전의 개수가 가장 최소

#제한이 10000이므로 10000개의 리스트를 만들고, 각 가치마다 dp로 업데이트 한다.