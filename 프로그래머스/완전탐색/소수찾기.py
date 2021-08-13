numbers = '975'
#numbers = [int(i) for i in numbers]
length = len(numbers)
# print(numbers)
caculatornum = []

from itertools import permutations
import math
# pool = ['A', 'B', 'C']
# print(list(map(''.join, permutations(numbers, 2))))

# def sosu(n):
#     if n == 0 or n == 1:
#         return False
#     else:
#         for i in (2, math.sqrt(n)+1):
#             if n % i == 0:
#                 return False
        
#         return True 

# def solution(numbers):
#     answer = []
#     for i in range(1, len(numbers)+1):              
#         arr = list(permutations(numbers, i))        # permutations(순열)을 사용해 i개씩 묶어지는 list 생성
#         print(arr)
#         for j in range(len(arr)):                   # 생성한 list(arr) 길이만큼 for문 실행
#             num = int(''.join(map(str,arr[j])))     # list(arr)의 값들은 tuple들로 되어있으모 join(map(str,))을 사용해 join해준다
#             print(num)
#             if sosu(num):                
#                 answer.append(num)                  # is_prime_number() 함수가 True일 경우 (= 소수일 경우) num 추가
    
#     answer = list(set(answer))                      # 같은 값이 나올 수 있기 때문에 set()을 통해 중복값 제거
#     return len(answer)

# def solution(numbers):
#     answer = 0
#     for i in range(1, len(numbers)+1):              
#         arr = list(map(''.join, permutations(list(numbers), i)))
#         print(arr)    
#         for num in list(set(arr)):
#             print(num)
#             if sosu(int(num)):                
#                 answer += 1                  
    
#     answer = list(set(answer))                      
#     return len(answer)

# print(solution(numbers))

import math
import itertools

# 소수인지 판별해주는 함수
def is_decimal(n):
    if n < 2: return False

    to = int(math.sqrt(n)) + 1
    for i in range(2, to):
        if n % i == 0: return False
    return True


# 정답 코드 
def solution(number):
    candidate = set()

    for i in range(len(number)):
        numbers = set(map(int, map(''.join, itertools.permutations(number, i+1))))
        candidate |= numbers # 합집합

    answer = 0
    candidate = list(candidate) # 리스트 변환
    for n in candidate:
        if is_decimal(n):
            answer += 1
    return answer