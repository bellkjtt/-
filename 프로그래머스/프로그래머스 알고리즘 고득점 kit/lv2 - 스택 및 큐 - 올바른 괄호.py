def solution(s):
    stack = []
    for j in s:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                return False
                break
    if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
        return True
    else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
        return False
    
    #stack에 대한 기본적인 이해가 필요한 문제.
    #가장 좋은 대표 문제이니 꼭 외워두자.
    #while문으로 짤 수도 있지만, 항상 무한루프에 주의하자.