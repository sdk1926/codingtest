import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))

minimum = min(array)
maximum = max(array)
print(minimum)
print(maximum)