문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

import sys
sys.stdin.readline()
b=list(map(int,sys.stdin.readline().split()))
count=0
for i in b:
    if i <=1: continue
    for j in range(2,int(i**(1/2))+1):
        if i%j==0 :break
    else:
        count+=1
        
print(count)

#소수의 개수는 sqrt(i)까지만 세더라도 셀 수 있다.
#이는 소인수분해값이 중간을 기준으로 나눠지기 때문이다.