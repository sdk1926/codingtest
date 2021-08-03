from typing import *


# 배열의 인덱스를 기준으로 인덱스 숫자를 제외한 왼쪽의 곱과 오른쪽들의 곱을 다시 곱한다. 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽곱셈
        for i in range(0,len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out 