n = int(input())
data = input().split()
x, y = 1, 1
direction = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in data:
    for j in range(len(direction)):
        if i == direction[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue 
    x , y = nx, ny         
            
print(x,y)

        
