array = [int(i)+sum(list(map(int, str(i)))) for i in range(1,10001) if int(i)+sum(list(map(int, str(i)))) <= 10000]
for i in range(1, 10001):
    if i not in array:
        print(i)
        