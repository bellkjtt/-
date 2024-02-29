https://school.programmers.co.kr/learn/courses/30/lessons/42584#

def solution(prices):
    
    ans=[]
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1,len(prices)):
            if prices[i]>prices[j]:
                ans.append(j-i)
                break
            else:
                cnt+=1
        else:
            ans.append(cnt)     
    
    answer = ans
    return answer

#자신보다 작은 게 나올 때까지 세면 된다.
#for else 문으로 만약 끝까지 간다면 확정시키기 가능