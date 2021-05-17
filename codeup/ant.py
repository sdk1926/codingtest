# 성실한 개미 6098
import sys
data = []
for i in range(10):
    data.append(list(map(int, sys.stdin.readline().split())))

x, y = 1, 1

while True:
    if data[x+1][y] == 1 and data[x][y+1] == 1:
        data[x][y] = 9
        break
    elif data[x][y] == 2:
        data[x][y] = 9
        break
    data[x][y] = 9
    if data[x][y+1] == 1:
        x +=1 
    elif data[x+1][y] == 1:
        y += 1
    else:
        y += 1 


for i in range(10):
    for j in range(10):
        print(data[i][j], end=' ')
    print()