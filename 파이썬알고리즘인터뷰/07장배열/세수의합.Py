from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        nums = [-1, 0, 1, 2, -1, -4]
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left, right = i + 1, len(nums) - 1
            while left < right:
                pass