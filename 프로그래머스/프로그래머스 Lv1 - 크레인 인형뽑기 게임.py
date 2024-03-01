https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    stack=[]
    cnt=0
    for i in moves:
        for j in board:
            if j[i-1]!=0:
                if stack and stack[-1]==j[i-1]:
                    stack.pop()
                    j[i-1]=0
                    cnt+=2
                    break
                else:
                    stack.append(j[i-1])
                    j[i-1]=0
                    break
    
    answer = cnt
    return answer

#보드를 돌면서 0이 아닌 위치를 찾고, 스택에 같은 게 있다면 pop
#그리고 카운트 증가
#아니라면 스택에 추가