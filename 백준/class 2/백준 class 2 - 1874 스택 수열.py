import sys
input=sys.stdin.readline
n = int(input())
ans =[]
num=0
cnt=[]
for _ in range(n):
    nin = int(input())
    #print(nin, num, ans)
    while num<=nin-1:
        ans.append('+')
        num+=1
        cnt.append(num)

    if cnt[-1]==nin:
        ans.append('-')
        cnt.pop()
    else:
        ans=False
        break

if ans==False:
    print('NO')
else:
    for i in ans:
        print(i)
#스택을 쌓아가면서, +가 나오면 1를 더하고, -가 나오면 pop을 한다.
#만약 ans가 비어있으면 No, 아니라면 전부 출력하면 된다.
