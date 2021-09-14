# import string

# tmp = string.digits+string.ascii_lowercase
# def convert(num, base) :
#     q, r = divmod(num, base)
#     if q == 0 :
#         return tmp[r] 
#     else :
#         return convert(q, base) + tmp[r]

# print(type(convert(437674,3)))

def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return int(rev_base[::-1])

# b = '211020101011'
# b = b.split('0')
# print(b)
c = '110011'
c = c.split('0')
print(c)
while '' in c:
    c.remove('')
print(c)

import math
def sosu(n):
    if n < 2: 
        return False

    num = int(math.sqrt(n)) + 1
    for i in range(2, num):
        if n % i == 0: 
            return False
    return True

answer = 0
for i in c:
    i = int(i)
    if sosu(i) == True:
        answer += 1

print(answer)
