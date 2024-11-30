import sys

n,c =list(map(int,sys.stdin.readline().split()))

arr=[int(i.rstrip()) for i in sys.stdin.readlines()]
arr.sort()
# print(n,c,arr)

def bi_search(array,value,low,high):
    mid = (low+high) //2
    if low>high:
        return mid
    res =[]
    res.append(array[0])
    for i in array:
        if i - res[-1]>=mid:
            res.append(i)
    # print(res)
    if len(res) >=c:
        return bi_search(array,value,mid+1,high)
    else:
        return bi_search(array,value,low,mid-1)

print(bi_search(arr,0,1,arr[-1]))

#거리의 최대를 이분탐색한다.
# arr[-1]-arr[0]부터 1까지로 시작한다.
#첫 공유기는 무조건 설치한다(array[0])
#거리가 mid보다 큰 녀석들을 res에 넣고,
#만약 C개가 되면 mid를 늘려서 해보고
#안된다면 mid를 줄여서 다시 해본다. 