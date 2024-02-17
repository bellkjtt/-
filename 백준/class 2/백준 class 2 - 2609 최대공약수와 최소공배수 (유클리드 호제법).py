import sys
a,b = map(int,sys.stdin.readline().split())
c=a%b
d=a*b
while b!=0:
    if (a%b)==0:
        c=b
        break
    c=a%b
    a=b
    b=c
    
print(c) #유클리드 호제법
print(int(d/c)) #최대공약수 * 최소공배수 = a*b와 같다.