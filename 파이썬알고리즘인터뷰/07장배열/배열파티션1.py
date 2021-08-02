from typing import *

# 파이써닉 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# 짝수 번째 값 계산 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0 
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n 
        
        return sum 

        