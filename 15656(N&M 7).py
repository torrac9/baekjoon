import sys

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
arr = []
num.sort()
def permutation():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in num: 
            #if i not in arr:
                arr.append(i) 
                permutation()
                arr.pop()
            
permutation()