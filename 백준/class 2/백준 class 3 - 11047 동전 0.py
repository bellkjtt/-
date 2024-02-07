#준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

#동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

#입력
#첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

#둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

#출력
#첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

#대표적인 그리드 문제
import sys

n,k = map(int,sys.stdin.readline().split())
li = [int(i.rstrip()) for i in sys.stdin.readlines() if int(i.rstrip())<=k] #K보다 낮은 것들만 리스트에 포함
li.sort(reverse=True)
s=0
for i in li:
    m=k//i
    s+=m
    k=k-i*m

print(s)

#몫을 구해서 더해주면 되므로 어려운 건 없다.
