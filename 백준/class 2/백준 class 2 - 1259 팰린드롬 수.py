import sys
while 1:
    li = sys.stdin.readline().rstrip()
    if li=='0':
        break
        
    if li==li[::-1]:
        print('yes')
    else:
        print('no')

#개인적으로 굉장히 쇼크 받았던 문제.
#인덱싱의 활용법을 절실히 깨닫게 된 문제이기도 했다
#아래는 인덱싱을 알기 전에 풀었던 코드
        
import sys
li = list(map(int,sys.stdin.buffer.read().rstrip().split()))
for i in li:
    if i==0:
        break
    i=str(i)
    a=0
    b=-1
    while len(i)!=a:
        if int(i)<10:
            print('yes')
            break
        a1=i[a]
        a2=i[b]
        if a1!=a2:
            print('no')
            break
        a+=1
        b-=1
        if len(i)==a:
            print('yes')