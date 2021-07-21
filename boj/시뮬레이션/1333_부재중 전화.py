# 내가 푼답 틀림!!
N, L, D = map(int, input().split(' '))

while True:
    i = 1
    if L < (D*i)+1 <= (L+5):
        print(D*i)
        break
    elif (D*i) > (L+5) and ((N*L)+((N-1)*5)) < (D*i):
        print(D*i)
        break
# 블로그 펌 
N, L, D = map(int, input().split())
res = ok = 0
i = 1
while i*D <= N*(L+5) - 5:
    if L <= i*D % (L+5) <= L+4:
        res = i*D
        ok = 1
        break
    i += 1
print(res if ok else ((N*(L+5) - 5)//D + 1) * D)