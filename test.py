n = int(input())

for i in range(n):
    word = input()
    word_list = word.split(" ")
    ans = [x[::-1] for x in word_list]
    for j in ans:
        print(j+" ")


