import sys
from collections import deque
n = int(input())
array = deque()
array = [input() for _ in range(n)]

for i in range(n):
    a = deque(array[i])
    b = []
    for j in range(len(a)):
        k = a.popleft()
        if k == '(':
            b.append(k)
        elif k == ')' and b:
            if b[-1] == '(':
                del b[-1]
            elif b[-1] == ')':
                print('NO')
                break
        
        elif not b and k == ')':
            print('NO')
            break
    if b:
        print('NO')
    elif not b and not a:
        print('YES')

# 시간초과 내일(0723) 다시풀기 