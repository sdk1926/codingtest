# 셸 정렬
# 셸 정렬은 단순 삽입 정렬의 장점은 살리고 단점을 보완하여 더 빠르게 정렬하는 알고리즘 이다. 

# 셸 정렬 알고리즘 구현하기 
from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """셸 정렬"""
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h 
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j + h] = tmp 
        h //= 2

if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num 

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x) # 배열 x를 셸 정렬 

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

## 셸 정렬 알고리즘 구하기 (h*3 +1 수열 사용 )

def shell_sort_ver2(a: MutableSequence) -> None:
    """셸 정렬(h * 3 + 1의 수열 사용)"""
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h,n):
            j = i - h 
            tmp = a[j]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp 
        h //= 3

if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num 

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort_ver2(x) # 배열 x를 셸 정렬 

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
