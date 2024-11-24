import sys

n,m = map(int,sys.stdin.readline().split())
li = [int(i.rstrip()) for i in sys.stdin.readlines()]
# print(li)
def cal(li,val):
    cnt=0
    for i in li:
        cnt+=i//val
    return cnt
# print(cal(li,271))

def bi_search(li, value, low, high):
    if low>high:
        return high
    mid = (low+high) //2
    #print(low,mid,high)
    #print(cal(li,mid),'이번 개수')
    if cal(li,mid) < value:
        return bi_search(li,value,low,mid-1)
    else:
        return bi_search(li,value,mid+1,high)


print(bi_search(li,m,1,max(li)))



#cal 해당 목표보다 작으면 Value에 도달하지 못한 것.
#처음 270이면 cal은 6이고, 따라서 mid는 더 작아져야 하므로 low~mid-1까지가 범위가 된다.
#그렇게 범위를 좁혀나가며 탐색한다.