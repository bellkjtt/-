from sys import stdin
t = stdin.readline().strip()
if t:
    print(t.count(" ")+1)
else:
    print(0)

#문장에서 단어의 개수를 구하려면 공백의 수에 +1을 해주면 된다.