# https://acmicpc.net/problem/2352
# 반도체 설계

import sys
from bisect import bisect_left
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = list(input_multiple_int())
lis = []
def LIS(n):
    for i in range(n):
        if i == 0 or lis[-1] < arr[i]:
            lis.append(arr[i])
        else:
            pos = bisect_left(lis, arr[i])
            lis[pos] = arr[i]

    print(len(lis))

LIS(N)