import sys
t=int(sys.stdin.readline())
for i in range(t):
    h,w,n=map(int, sys.stdin.readline().split())
    a=n%h
    b=(n//h)+1

    if n%h==0:
        a=h
        b=n//h
        print(a*100+b)
    else:
        print(a*100+b)

#호텔의 호수는 저절로 채워지므로 몫을 구해주면 층수는 저절로 구해진다.
#따라서 층수 *100+b를 해주면 되고, 몫이 0일때는 최상층이므로 그때만 예외처리

import sys
t=int(sys.stdin.readline())
for i in range(t):
    h,w,n=map(int, sys.stdin.readline().split())

    if n%h==0:
        print(h*100+n//h)
    else:
        print(n%h*100+n//h+1)

#모범적인 프로그래밍
#아예 h때만 넣는 방식을 택했다.