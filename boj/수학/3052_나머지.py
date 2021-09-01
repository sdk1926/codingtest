import sys
n = 10 
data = [sys.stdin.readline().strip() for i in range(n)]
a = set([int(i) % 42 for i in data])
print(len(a))                            