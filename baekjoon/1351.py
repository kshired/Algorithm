# https://acmicpc.net/problem/1351
# 무한 수열
from collections import defaultdict
import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

dp = defaultdict(int)

N,P,Q = input_multiple_int()

def solve(n):
    if n == 0:
        return 1
    if dp[n] == 0:
        dp[n] = solve(n//P) + solve(n//Q)
        return dp[n]
    else:
        return dp[n]
    
print(solve(N))