n,a,b = map(int,input().split())
cnt=0
while a!=b:
    a-=a//2
    b-=b//2
    cnt+=1
print(cnt)

#짝수 =/2 홀수 =+1 후에 /2

n,a,b = map(int,input().split())

cnt=0
while a!=b:
    if a%2==0 and b%2==0:
        a=a/2
        b=b/2
        cnt+=1
    elif a%2==1 and b%2==0:
        a=(a+1)/2
        b=b/2
        cnt+=1
    elif a%2==0 and b%2==1:
        a=a/2
        b=(b+1)/2
        cnt+=1
    else:
        a=(a+1)/2
        b=(b+1)/2
        cnt+=1

print(cnt)