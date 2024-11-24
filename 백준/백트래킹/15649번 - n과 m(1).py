n,m = map(int,input().split())

nums =[i for i in range(n)]

def dfs(visited):
    if len(visited)==m:
        print(' '.join(map(str,visited)))
        return
    q=[]
    for num in range(1,n+1):
        if num not in visited:
            visited.append(num)
            dfs(visited)
            visited.pop()
dfs([])

#vistied에 없다면 해당 num을 더해준다.
#그 후에 len 조건이 다 찼는지 검사하고,
#만약에 다 찼다면 직전은 pop해서 다시 채워넣는다.
#끝까지 갔다면 다시 num이 2로 올라가서 반복된다.