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
