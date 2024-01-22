a,b = map(int,input().split())

if a-1>=0 and b-45<0:#알람 시계가 0부터 45분이라면  시간을 1빼야함
    a=a-1
    print(a,15+b)
elif a-1<0 and b-45<0: #만약 24시면 예외처리
    a=23+a
    print(a,15+b)
else:
    print(a,b-45)

