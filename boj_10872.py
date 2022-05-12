# 팩토리얼 재귀로 풀기
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input())
print(factorial(n))