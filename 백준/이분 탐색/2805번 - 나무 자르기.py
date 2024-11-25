n,m = map(int,input().split())

li= [int(i) for i in input().split()]

#print(n,m)
#print(li)

def cal(array,val):
    cnt=0
    for i in array:
        if i>val:
            cnt+=i-val
    return cnt
    

def bi_search(array, value, low, high):
    mid = (low + high)//2
    if low>high:
        return mid
    if cal(array,mid)>value:
        return bi_search(array,value,mid+1,high)
    elif cal(array, mid)<value:
        return bi_search(array,value,low,mid-1)
    else:
        return mid

print(bi_search(li,m,1,max(li)))

#기존 이분탐색과 같으나, 유의해야 하는 점은 
# low>high일 때 mid를 반환한다는 것이다.
# 왜냐하면 해당 값 일 때 최소 m이 반환되어야 하기 때문에
# low를 반환해도 안되고, high를 반환해도 안된다.
# 대표적으로 n=2, m=1, [2 2] 면 low=1, high=2인데 
# 마지막에 2>1일 때 1이 나와야 한다. 하지만 low면 2가 나온다.