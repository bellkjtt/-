def pascals_p(n):
    pyramid = []
    for i in range(n):
        layer = []
        for j in range(i + 1):
            if j == 0 or j == i:
                layer.append(1)  # 각 층의 맨 앞과 맨 끝은 항상 1
            else:
                layer.append(pyramid[i-1][j-1] + pyramid[i-1][j])  # 윗층의 왼쪽과 오른쪽 값을 더해서 채움
        pyramid.append(layer)
    return pyramid

n = int(input())
pyramid_n = pascals_p(n)
pyramid_n_1 = pascals_p(n-1)



def py(pyramid_n,pyramid_n_1):
    pyramid_n = list(map(list,pyramid_n))
    pyramid_n_1 = list(map(list,pyramid_n_1))
    for i in range(len(pyramid_n_1)):
        pyramid_n_1[i].insert(0,0)
        pyramid_n_1[i].append(0)
    # print(pyramid_n,'현재단계')
    # print(pyramid_n_1,'전단계')
    for j in range(1,len(pyramid_n)-1):
            for k in range(len(pyramid_n[j])):
                pyramid_n[j][k]+=pyramid_n_1[j-1][k]+pyramid_n_1[j-1][k+1]
    return pyramid_n

q=pascals_p(3)
q_1=pascals_p(2)
for v in range(2,n):
    # print(py(pyramid_n,pyramid_n_1),'최후값')
    
    q=py(q,q_1)
    q.append(pascals_p(v+2)[-1])
    q_1=q

if n==1:
    print(1)
else:
    for z in range(len(q)-2,-1,-1):
        print(' '.join(map(str,q[z])))
    




