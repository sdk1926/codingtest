import sys
from collections import deque
n = int(input())
for i in range(n):
    data    = deque(map(int,sys.stdin.readline().split()))
    len_num = data.popleft()
    avg     = sum(data) / len_num
    count   = len([i for i in data if i > avg])
    ans     = count/len_num * 100
    print(f"{ans:.3f}%")