def solution(s):
    answer=0
    m=len(s)
    for i in range(m):
        stack = [ ]
        for j in range(m):
            c=s[(i+j)%m]
            if c == "(" or c=="[" or c=="{" :
                stack.append(c)
            else:
                if not stack:
                    break

                if stack[-1]=='(' and c == ")":
                    stack.pop()
                elif stack[-1]=='[' and c == "]":
                    stack.pop()
                elif stack[-1]=='{' and c == "}":
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer+=1
        
    return answer

#스택에 대해서 for문 돌리기
#for else문도 사용 가능하다는 것을 알았다.
#return은 줄을 잘 맞춰줘야 한다.