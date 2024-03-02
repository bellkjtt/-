https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque
def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    for val in goal:
        if val in q1:
            k=q1.popleft()
            if k!=val:
                answer = 'No'
                break
                
        else:
            k=q2.popleft()
            if k!=val:
                answer='No'
                break
    else:
        answer = 'Yes'
    
    return answer

#단어를 뽑으면서 만약 같지 않다면 바로 break
#for else로 끝에 도달하면 yes 