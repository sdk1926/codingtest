# isedol
import sys 
data = []
n = 19

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

count = int(input())
for i in range(count):
    x,y = map(int, input().split())
    for j in range(19):
        if data[j][y-1] == 0:
            data[j][y-1] = 1
        else:
            data[j][y-1] = 0
        
        if data[x-1][j] ==0:
            data[x-1][j] = 1
        else:
            data[x-1][j] = 0 

for i in range(n):
    for j in range(n):
        print(data[i][j], end=' ')
    print()