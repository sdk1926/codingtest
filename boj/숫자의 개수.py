# 내가 쓴 답 
a = int(input())
b = int(input())
c = int(input())

d = list(str(a * b * c))
e = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(d)):
    g = int(d.pop())
    for j in range(10):
        if g == j:
            e[j] += 1
            break 

for k in e:
    print(k) 

# 효율적인 코드 
a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))


# count 함수