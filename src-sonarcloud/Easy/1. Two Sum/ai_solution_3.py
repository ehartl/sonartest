from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nums[:index]:
                return [nums.index(complement), index]
            indices.append(index)
        return []