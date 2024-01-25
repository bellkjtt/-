a = list(map(int,input().split()))
b = [i for i in range(1,9)]
c = [i for i in range(8,0,-1)]
count=0
for i in range(8):
    if b[i]==int(a[i]):
        count+=1
    elif c[i]==int(a[i]):
        count-=1
if count==8:
    print('ascending')
elif count==-8:
    print('descending')
else:
    print('mixed')
# if를 사용하는 게 가장 효율이 좋다.
# 시간복잡도 nlog(n)