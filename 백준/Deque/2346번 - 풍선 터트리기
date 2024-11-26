from collections import deque

n = int(input())
li = deque(map(int, input().split()))

num = deque([i for i in range(2,n+1)])

# print(li)
# print(num)
ans =[1]
k=0
for i in range(n-1):
    w = li.popleft()

 
    if w>=0:
        for j in range(w-1):
            li.append(li.popleft())
        for i in range(w-1):
            num.append(num.popleft())
    
    else:
        for j in range(abs(w)):
            li.appendleft(li.pop())
        for i in range(abs(w)):
            num.appendleft(num.pop())
    # print(w,num,li,'현재 상태')
    # print(num,"바뀐 숫자")
    ans.append(num.popleft())
    # print(num,'마지막 상태')
        
    
print(' '.join(map(str,ans)))    
    
#덱의 특성을 고려해서 앞에서 빼서 뒤로 하거나, 뒤에서 빼서 앞으로 넣는다.
#appendleft와 pop, append와 popleft의 조합임을 명심한다.