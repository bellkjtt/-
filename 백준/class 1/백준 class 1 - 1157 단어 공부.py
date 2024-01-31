#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 
#가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
#단, 대문자와 소문자를 구분하지 않는다.
#조건 : 단어의 길이 100만

import sys
input =sys.stdin.readline
t = input().strip().upper() #모든 문자를 대문자로 통일 (구분하지 않는다)
k =list(set(t)) #알파벳 종류 구하기
v =[]
for i in k:
    v.append(t.count(i)) #t에서 각각의 개수 세기
q=max(v)
if v.count(q)>1:
    print('?')
else:
    print(k[v.index(q)])

#일부러 for과 if를 나누었다. 시간복잡도 고려