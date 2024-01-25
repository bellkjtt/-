a = int(input())
for i in range(a):
    b, c = input().split()
    q =''
    for j in c:
        q+= int(b)*j
    print(q)