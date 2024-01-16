def solution(participant, completion):
    participant.sort()
    completion.sort() #sort를 통해 정렬
    completion.append(0)
    answer=0
    a=dict() #dict 함수로 해싱을 만들어줌. 이유는 메모리 관리 용이
    for i in range(len(participant)):
        a[participant[i]]=completion[i] #paticipant와 completion 두개 비교
    for i in a:
        if i!=a.get(i): #만약 두개 비교 했을 때 다르면 그 사람이 완주 못한 사람
            answer=i
            break
    return answer
