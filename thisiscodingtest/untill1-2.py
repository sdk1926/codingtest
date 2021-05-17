# 1이 될때까지 2 (배수 활용하기)

n,k = map(int, input().split())
result = 0 

while True:
    target = (n // k) * k 
    result += (n - target)
    n = target 
    if n < k:
        break
    result += 1
    n //= k 

result += (n-1)
print(result)