# https://programmers.co.kr/learn/courses/30/lessons/12954
# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return [i*x for i in range(1,n+1)]