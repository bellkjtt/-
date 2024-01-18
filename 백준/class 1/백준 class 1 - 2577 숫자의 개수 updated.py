#세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
#예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

import sys
from functools import reduce

def multiply(arr):
    return reduce(lambda x, y: x * y, arr) #전부 곱하는 함수

a= list(map(int,sys.stdin.buffer.read().rstrip().split()))
b = list(map(int,(str(multiply(a))))) #전부 곱해서 리스트로 만든다.
c= [0 for _ in range(10)]
for i in b:
    c[i]+=1
print(*c,sep='\n')

#24.01.16 
#조금 더 pythonic 한 풀이로 바뀌었다.
#list comprehention을 사용

#아래는 2년 전 풀이

k=1
for i in range(3):
    n=int(input())
    k*=n #리스트를 전부 곱한다

b = list(set(str(k)))

c=['False']*(10-len(b))
d = (b+c)
e=[]

for i in range(10):
    if str(i) in d:
        e.append(str(k).count(str(i)))
    else:
        e.append(0)
    print(e[i])


    

