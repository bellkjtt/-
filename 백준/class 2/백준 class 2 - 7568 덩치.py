import sys
input = sys.stdin.readline

a = int(input())
b = [list(map(int,input().split())) for _ in range(a)]
b_1 = [i for i in b]

#수학적 정의 : 자신보다 키와 덩치가 큰 사람의 수+1 = 자신의 등수
ans =[]
for i,j in b:
    count=0
    for k,l in b:
        if i<k and j<l:
            #print(i,k,'|',j,l)
            count+=1
    ans.append(count+1)

print(' '.join(map(str,ans)))

#구현 문제는 수학적 정의를 알고 풀지 않으면 개고생한다..