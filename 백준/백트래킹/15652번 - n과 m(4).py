n,m = map(int,input().split())

nums =[i for i in range(n)]
s=[]
def dfs(start): 
    if len(s)==m:
        print(' '.join(map(str,s))) 
        return

    for num in range(start,n+1):
            s.append(num)
            dfs(num)
            s.pop()


dfs(1)

#n과 m 3번에서 start를 넣어주면 해당 start부터 시작하게 된다.
#따라서 다음 시작 때는 1이 더해져서 출력이 된다.