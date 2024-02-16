import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2).T
    ans=[]
    for i in arr1:
        cnt=[]
        for j in range(len(arr2)):
            cnt.append(int(sum(i*arr2[j]).tolist()))
        ans.append(cnt)
        
    answer = ans
    return answer