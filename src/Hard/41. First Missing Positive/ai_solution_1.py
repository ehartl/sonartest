from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Mark numbers (num < 1) and (num > n) with a special marker number (n+1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark each cell appearing in the array
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Step 3: Find the first cell which isn't negative (i.e., the first missing positive)
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1