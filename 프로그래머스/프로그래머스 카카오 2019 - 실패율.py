https://school.programmers.co.kr/learn/courses/30/lessons/42889#

def solution(N, stages):
    stages.sort()
    ans=[]
    ans2=[]
    dp=len(stages)
    for i in range(1,N+1):
        j = stages.count(i)
        if j!=0:
            ans.append(j/dp)
        else:
            ans.append(0)
        dp-=j 
    ans2=[]
    for _ in ans:
        k = ans.index(max(ans))
        ans[k]=-1
        ans2.append(k+1)
    answer = ans2
    return answer

#실패율을 먼저 구하고, 가장 큰 값을 대체해가면서 가장 큰 index 번호를 찾는다.