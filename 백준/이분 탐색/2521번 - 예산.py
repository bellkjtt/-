import sys

n = sys.stdin.readline()

arr = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
def cal(array,mid):
    cnt=0
    for i in array:
        # print(i)
        if i>mid:
            cnt+=mid
        else:
            cnt+=i
    return cnt

# print(cal(arr,127))

def bi_search(array,value,low,high):
    mid = (low + high)//2
    if low>high:
        return mid
    if cal(array,mid)>value:
        return bi_search(array,value,low,mid-1)
    else:
        return bi_search(array,value,mid+1,high)

if sum(arr)<=m:
    print(max(arr))
else:
    print(bi_search(arr,m,1,max(arr)))

#예산의 총합을 Cal로 두고, 해당 value를 찾는다.
#만약 이미 sum이 해당된다면 arr에서 최대값 출력을 해준다.