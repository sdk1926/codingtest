import math

n = int(input())
a = list(map(int, input().split()))

def is_decimal(n):
    if n < 2: return False

    to = int(math.sqrt(n)) + 1
    for i in range(2, to):
        if n % i == 0: return False
    return True

i = 0     
for j in a:
    if is_decimal(j):
        i += 1

print(i)