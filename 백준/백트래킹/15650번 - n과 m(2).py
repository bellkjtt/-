n,m = map(int,input().split())

nums =[i for i in range(n)]

def dfs(visited,q): 
    if len(visited)==m:
        #print(visited)
        q.add(tuple(sorted(visited)))    
        return

    for num in range(1,n+1):
        if num not in visited:
            visited.append(num)
            dfs(visited,q)
            visited.pop()
    return q


a= sorted(dfs([],set()))
for i in a:
    print(' '.join(map(str,i)))

#n과 m 번에서, q를 따로 set으로 만들어서 리스트화해준다.
#다른 방법도 있으나 일단 이걸로 풀었다.