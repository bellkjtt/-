import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3) 
    L = []  
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))


#가장 base case는 k=0일 때 * 하나만 찍히는 것이다.
#그리고 리스트를 만든다. N에 따라 처음 리스트가 만들어지는데,
#그 리스트에 있는 것들을 3번 반복하고,
#두번쨰 줄은 공백을 추가하여 반복하고,
#세번째 줄은 첫번쨰 줄과 같이 3번 반복한다.
#9가 들어가도 n-1 리스트는 만들어지므로 똑같이 만들 수 있다. 