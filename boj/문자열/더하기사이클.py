n = int(input())
m = list(str(n))

i = j = k = 0
if n < 10:
    i = 0 
    j = int(m[0])
else:
    i = int(m[0]) 
    j = int(m[1])
k = i + j 
count = 1 

while True:
    if n == 0:
        break
    count += 1
    i = j
    j = k
    k = (i + j) % 10
    ans = (j*10) + k
    if ans == n:
        break 
print(count)