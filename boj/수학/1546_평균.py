import sys
n = int(input())
data = list(map(int,sys.stdin.readline().split()))
max_num = max(data)
data2 = [(i/max_num) * 100 for i in data]
ans = sum(data2) / n
print(ans)