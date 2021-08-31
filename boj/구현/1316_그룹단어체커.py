n = int(input())
arr = []
for i in range(n):
    arr.append(input())

def judgement(string):
    array = []
    for i in string:
        if array and array[-1] != i and i in array:
            return 0
        array.append(i)
    return 1

ans = 0 

for i in arr:
    ans += judgement(i)

print(ans)


