# 퀵 정렬 

# 배열을 두 그룹으로 나누기 
from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """배열을 나누어 출력"""
    n = len(a)
    pl = 0 # 왼쪽 커서
    pr = n - 1 # 오른쪽커서 
    x = a[n // 2] # 피벗(가운데 원소)
    
    

    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')
    print(*a[0 : pl])   # a[0]~a[pl-1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl])  # a[pr + 1]~a[pl-1]
    
    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1 : n])  # a[pr+1]~a[n-1]

if __name__=='__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소수가 num인 배열을 생성 

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)

# 퀵 정렬 알고리즘 구현하기 

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left]~a[right]를 퀵 정렬"""
    pl = left # 왼쪽 커서 
    pr = right # 오른쪽 커서 
    x = a[(left + right) // 2] # 피벗(가운데 원소)

    print(f'a[{left}]~a[{right}]: ', a[left: right +1]) # 새로 추가된 부분 
    
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a)-1)

if __name__=='__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요'))
    x = [None] * num # 원소 수가 num인 배열을 생성 

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')