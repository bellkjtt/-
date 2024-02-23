def sol():
    a=[None]*2000001
    b=map(int,open(0))
    next(b)
    for i in b:
        a[i]=1
    print("\n".join(str(i) for i in range(-1000000,1000001,1) if a[i]))

sol()

#-100만부터 100만까지 출력하는데,그 값이 a[i]일 때만 출력함.
#리스트를 따로 만들어서, 그 리스트의 인덱스에 해당하는 열만 1로 활성화.
#메모리 제한 때문에 200만 제한을 둠.