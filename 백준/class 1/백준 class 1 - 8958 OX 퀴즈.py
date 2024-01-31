t = int(input())
k = [input() for i in range(t)] #OX 리스트를 t개 입력받는다.
for i in range(t):
    if k[i][0]=='O':  #i 번째 리스트의 첫번째가 O인지 판별
        num=1
        count=1
    else: 
        num=0
        count=1
    for j in range(len(k[i])-1): #그 리스트 길이의 -1까지 순환
        if k[i][j]=='O' and k[i][j+1]=='O': #O 다음에 O라면
             count+=1 #숫자 증가
             num+=count #num은 count만큼 점수가 오른다
        elif k[i][j+1]=='O': num+=1  #만약 뒤만 O라면 num만 1 증가
        elif k[i][j]=='O' and k[i][j+1]=='X': count=1 #만약 앞이 O, 뒤가 X라면 count는 1로 초기화 
    print(num)