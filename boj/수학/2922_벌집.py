n = int(input())

ans = 1
range_num = 1

while True:
    if range_num >= n:
        break
    range_num += (6 * ans)
    ans += 1
print(ans)