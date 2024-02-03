#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#단, 중복된 단어는 하나만 남기고 제거해야 한다.

import sys

a,*b = map(str,sys.stdin.read().split())
c=[]
for i in b:
    c.append(len(i))  #각각의 len을 구한다
dic ={}
for i in range(len(b)):
    dic[b[i]]=c[i] #중복 제거 및 길이 추가
d=sorted(dic.items(),  key = lambda item: item[0]) #item의 순서에 따라 sort
e=sorted(d, key = lambda item: item[1]) #len에 따라 sort
for i in range(len(e)):
    print(e[i][0])