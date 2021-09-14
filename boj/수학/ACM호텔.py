n = int(input())
for i in range(n):
    H, W, N = map(int, input().split())
    if N % H == 0:
        room = H * 100
        number = N // H
    else:
        room = (N % H) * 100 
        number = (N // H) + 1
    print(room + number)