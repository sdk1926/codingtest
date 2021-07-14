import sys 

n, m = map(int, input().split())
d = [[0] * 4 for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1
gamelist = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    gamelist.append(list(map(int, sys.stdin.readline().split())))

count = 1 
changedirection = 0 

def direction_change():
    global direction
    direction -=1
    if direction == -1:
        direction = 3 

while True:
    direction_change()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and gamelist[nx][ny] == 0:
        d[nx][ny] = 1
        gamelist[nx][ny] = 1
        x , y = nx, ny 
        count += 1 
        changedirection = 0 
        continue 
    else:
        changedirection += 1
    
    if changedirection == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if gamelist[nx][ny] == 0:
            x,y = nx, ny 
        else:
            break 
        changedirection = 0 

print(count)
