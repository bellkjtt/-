def solution(nums):
    k=len(set(nums))
    if k<(len(nums)/2):
        answer=k
    else:
        answer=len(nums)/2
    return answer

#포켓몬 종류가 총 포켓몬 수의 2분의 1보다 낮다면
#그 수는 k가 되고, 아니라면 최대 고를 수 있는 종류는 총 수의 2분의 1이다.
#이게 가능한 이유는 N/2 마리를 선택하는 게 고정되어 있기 때문이다.
#수학적 풀이가 더 합리적으로 보이기에 이렇게 풀었다.