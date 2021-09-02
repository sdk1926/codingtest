n = int(input())
default = 99
def 판별(list):
    m = list[1] - list[0]
    for i in range(len(list)-1):
        k = list[i+1] - list[i]
        if k == m:
            m = k 
        else:
            return 0
    return 1 

if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        a = list(map(int, str(i)))
        default += 판별(a)
    print(default)