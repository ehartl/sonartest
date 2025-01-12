from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                return [nums.index(complement), index]
            num_set.add(num)
        return []