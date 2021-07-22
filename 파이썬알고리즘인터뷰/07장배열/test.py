from typing import *

## 두수의 합 

# 부르트 포스트 풀이 방법
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# in연산으로 시간 줄이기 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement)+ (i+1)]

# 첫 번째 수를 뺀 결과 키 조회 
