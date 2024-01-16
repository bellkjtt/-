def solution(arr):
    ans =[]
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            ans.append(arr[i])
    ans.append(arr[len(arr)-1]) #마지막 항 추가
    answer=ans
    return answer

#set을 사용하면 순서가 지켜지지 않는다.
#따라서 앞에서부터 비교해서 뒤쪽이 다르다면 추가, 아니면 뺀다.
#while을 사용한다면 더 좋은 코드를 짤 수 있을 것.