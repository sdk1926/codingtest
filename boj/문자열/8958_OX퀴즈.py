from collections import deque
array = deque()
n = int(input())
for _ in range(n):
    a = str(input())
    array.append(a)

for _ in range(n):
    elm = list(array.popleft())
    count = 0 
    i = 0
    for j in elm:
        if j == 'O':
            i += 1
            count += i
        else:
            i = 0 
    print(count)
