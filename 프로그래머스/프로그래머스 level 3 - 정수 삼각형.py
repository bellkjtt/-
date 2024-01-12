def solution(triangle):
    h=len(triangle)
    q=triangle
    while h>1:
        for i in range(h-1):
            dp=max(q[h-1][i],q[h-1][i+1])
            q[h-2][i]+=dp
        h-=1
        
    answer = q[0][0]
    return answer
#깔끔하게 바꾼 코드

def solution(triangle):
    s_b=0
    s=0
    q=list(reversed(triangle))
    q.append(0)
    for i in range(len(q)-1):

        k1=q[i]
        k2=q[i+1]
        for j in range(len(k1)-1):
            dp=max(k1[j],k1[j+1])
            k2[j]+=dp

    answer = k1[0]
    return answer
#처음 푼 코드