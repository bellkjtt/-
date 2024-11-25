n,m = map(int,input().split())

nums =[i for i in range(n)]
s=[]
def dfs(): 
    if len(s)==m:
        print(' '.join(map(str,s))) 
        return

    for num in range(1,n+1):
            s.append(num)
            dfs()
            s.pop()


dfs()

#n과 m 1번에서 그냥 if 조건만 빼면 전체가 출력된다.
#num이 있든 없든 출력하므로 조건만 지워주면 된다.
#len이 끝에 다다랐다면 백트래킹을 위해 계속 pop 해준다.