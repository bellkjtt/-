import sys
input=sys.stdin.readline

T = int(input())
a = [int(input()) for _ in range(T)]

ans =[]

m = [25,10,5,1]
c, cnt=0,0
k=[]

for i in a:
    for j in range(4):
        c = i//m[j]
        i-=c*m[j]
        ans.append(c)

for i in range(1,len(ans)+1):
    print(ans[i-1], end=' ')
    if i%4==0:
        print(sep='')
        