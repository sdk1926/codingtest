import sys
a,b = sys.stdin.readline().split()
a,b = int(a[::-1]), int(b[::-1])
print(max(a,b))