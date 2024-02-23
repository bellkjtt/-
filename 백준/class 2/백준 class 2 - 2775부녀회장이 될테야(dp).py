a-1층에 있는 사람들을 고려해야 하므로 dp로 풀어야한다.

import sys
a= int(sys.stdin.readline())
c=[]
d=0
ans=0
for _ in range(a):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())

    k_count=1
    n_count=n
    dp=[i for i in range(1,n_count+1)]
    if k==1:
        ans=sum([i for i in range(1,n_count+1)])
        print(ans)
    else:
        while k_count!=k:
            dp2=[sum(dp[0:j]) for j in range(1,n_count+1)]
            dp=dp2 #다이나믹 프로그래밍 ( 전의 수를 기억하고 다시 쓴다)
            k_count+=1
            ans=sum(dp2)
        print(ans)
