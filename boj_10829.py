n = int(input())
def binary(n):
    if n==0:
        return ''
    mok = n//2
    return binary(mok) + str(n%2)
print(binary(n))