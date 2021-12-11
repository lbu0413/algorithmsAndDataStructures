a, b = map(int, input().split())


# 최대공약수 구하는 방법.
# a와 b가 있고 a가 더 큰 숫자라고 할 때
# a를 b로 나눈 나머지 = r
# a, b의 gcd == r, b의 gcd

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
