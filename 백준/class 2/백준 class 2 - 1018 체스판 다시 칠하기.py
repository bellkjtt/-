n, m = map(int,input().split())
chess= [input() for _ in range(n)]



W = ['WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW']

B= ['BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB'] #비교를 위한 세트들


def su(i,j): #전체를 비교해가면서 카운트를 증가시킨다.
    re_w=0
    re_b=0
    for di in range(8):
        for dj in range(8):
            ni, nj = i+di, j+dj
            if chess[ni][nj]!=W[di][dj]: #다시 칠해야 하는 흰 사각형의 개수
                re_w+=1
            if chess[ni][nj]!=B[di][dj]: #다시 칠해야 하는 검은 사각형의 개수
                re_b+=1
    return min(re_w,re_b)  #둘 중에 작은 것을 리턴


result=100000000
for i in range(n-7):
    for j in range(m-7):
        result=min(result,su(i,j)) #매번 갱신
        
print(result)

