n = int(input())
array = list(map(int, input().split(' ')))

array.sort()
answer = 0
answer2 = 0
for i in range(len(array)):
    answer = (answer + array[i])
    answer2 += answer

print(answer2)