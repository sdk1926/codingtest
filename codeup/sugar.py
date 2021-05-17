# 설창과자 봅기
n,m = map(int, input().split())
data = []
for i in range(n):
    data.append([])
    for j in range(m):
        data[i].append(0)

count = int(input())
for i in range(count):
    l, d, x, y = map(int, input().split())
    data[x-1][y-1] = 1
    if d == 0:
        for j in range(1,l):
            data[x-1][(y+j)-1] = 1
    else: 
        for p in range(1, l):
            data[(x+p)-1][y-1] = 1 

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()
