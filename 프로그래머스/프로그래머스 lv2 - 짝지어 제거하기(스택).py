https://school.programmers.co.kr/learn/courses/30/lessons/12973#

def solution(s):
    answer = -1
    stack =[]
    for i in s:
        c=i
        if not stack:
            stack.append(i)
            # print(stack,'맨위쪽')
        elif i in stack and stack[-1]==i:
            # print(stack,'위쪽')
            stack.pop()
        else:
            # print(stack,'아래쪽')
            stack.append(i)
    # print(stack)    
        
    if not stack:
        answer=1
        return answer
    else:
        answer=0
        return answer
    
    
    #abbba같은게 있다면, 스택에 있는지 일단 살펴보고, 
    #그 스택의 마지막 문자가 현재 문자와 같다면 튀어나오게 만든다