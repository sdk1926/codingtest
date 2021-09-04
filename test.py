import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == 0 and b == c:
    print(1)
if b > c:
    print(-1)

print(a // (c-b) +1)