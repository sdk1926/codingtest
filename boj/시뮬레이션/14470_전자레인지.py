a = int(input())  # 원래 고기의 온도 
b = int(input())  # 목표 온도 
c = int(input())  # 언 고기를 고기를 1도 데우는데 걸리는 시간 
d = int(input())  # 해동하는데 걸리는 시간 
e = int(input())  # 해동 된 고기가 데워지는 데 걸리는 시간

if a > 0:
    answer = (b - a) * e
    print(answer)
elif a < 0:
    answer = ((0 - a) * c) + (d) + (b * e)
    print(answer)