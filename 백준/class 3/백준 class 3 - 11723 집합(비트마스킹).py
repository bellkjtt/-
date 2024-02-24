import sys
m = int(sys.stdin.readline())
s=set()
for _ in range(m):
    k = sys.stdin.readline().rstrip().split()
    if len(k)==2:
        com,x=k
        ix=int(x)
        s1=set([ix])
        if com=='add':
            s=s | s1
        elif com=='remove':
            s=s-s1
        elif com=='check' and (ix in s):
            print(1)
        elif com=='check' and (ix not in s):
            print(0)
        elif com=='toggle' and (ix in s):
            s=s-s1
        elif com=='toggle' and (ix not in s):
            s=s | s1
            
    else:
        com=k[0]
        if com =='all':
            s=set(i for i in range(1,21))
        elif com=='empty':
            s=set()

#set을 활용하면 비트마스킹을 이용하지 않더라도 연산 효과가 비슷하다.
#다만 비트마스킹 측면으로 각 비트를 자리수로 표현할 수도 있긴 하다. 1256=110011