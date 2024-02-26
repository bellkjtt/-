https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    cor=[]
    dp1,dp2=0,0
    cnt=0
    for a in dirs:
        tmp=[]
        if a=="U" and dp2<=4:
            dp2+=1
            if (dp1,dp2-1,dp1,dp2) not in cor and ( (dp1,dp2, dp1,dp2-1) not in cor):
                cor.append((dp1,dp2-1,dp1,dp2))
                
        if a=="D" and dp2>=-4:
            dp2-=1
            if (dp1,dp2+1,dp1,dp2) not in cor and ( (dp1,dp2,dp1,dp2+1) not in cor):
                cor.append((dp1,dp2+1,dp1,dp2))
                
        if a=="L" and dp1>=-4:
            dp1-=1
            if ((dp1+1,dp2,dp1,dp2) not in cor) and ( (dp1,dp2,dp1+1,dp2) not in cor):
                cor.append((dp1+1,dp2,dp1,dp2))
            
        if a=="R" and dp1<=4:
            dp1+=1
            if (dp1-1,dp2,dp1,dp2) not in cor and ( (dp1,dp2,dp1-1,dp2) not in cor):
                cor.append((dp1-1,dp2,dp1,dp2))
 
    print(cor)

    answer = len(cor)
    return answer

#경로에 대한 걸 차원으로 표시하여 시간복잡도 줄이기
#앞뒤에 대한 고려를 동시에 한다.