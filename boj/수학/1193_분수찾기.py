# 내풀이 
x = int(input())

def fac(n):
    count1 = 0
    num_count1 = 0
    while count1 < n:
        count1 += 1
        num_count1 += count1
    return num_count1

num_count = 0 
count = 0
while num_count < x:
    count += 1
    num_count += count

chai = x - fac(count-1)

if count % 2 == 0:
    bunja = 1
    bunmo = count
    for _ in range(chai-1):
        bunja += 1
        bunmo -= 1
    print(f'{bunja}/{bunmo}') 
elif count % 2 != 0:
    bunja = count
    bunmo = 1
    for _ in range(chai-1):
        bunja -= 1
        bunmo += 1
    print(f'{bunja}/{bunmo}') 

# 핵 천재 풀이 
# X 값을 빼면서 몇번째 줄에 몇번째 까지인지 구함 
X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')

# 인간계 풀이
input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  

gap = max_num - input_num 
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print(f'{top}/{under}')