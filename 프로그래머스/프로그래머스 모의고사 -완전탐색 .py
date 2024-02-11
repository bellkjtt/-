https://school.programmers.co.kr/learn/courses/30/lessons/42840#

def solution(answers):
    x1 = [1,2,3,4,5]
    x2 = [2,1,2,3,2,4,2,5]
    x3 = [3,3,1,1,2,2,4,4,5,5]
    y1=[]
    y2=[]
    y3=[]
    for i in range(len(answers)):
        y1.append(x1[i%5])
        y2.append(x2[i%8])
        y3.append(x3[i%10])
    k = [0,0,0]
    for i in range(len(answers)):
        if y1[i]==answers[i]:
            k[0]+=1
        if y2[i]==answers[i]:
            k[1]+=1
        if y3[i]==answers[i]:
            k[2]+=1
    answer = []
    for idx,m in enumerate(k):
        if k[idx]==max(k):
            answer.append(idx+1)
    print(answer)
    return answer

#enumerate의 중요성을 알 수 있다.
#사실 위 함수도 enumerate를 활용한다면 더 줄일 수 있다.