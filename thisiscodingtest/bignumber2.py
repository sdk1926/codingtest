# 큰 수의 법칙 풀이2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

bignumber = first * int(m / (k + 1)) * k + m % (k + 1)
secondnumber = second * int(m // (k + 1))

result = bignumber + secondnumber

print(result)