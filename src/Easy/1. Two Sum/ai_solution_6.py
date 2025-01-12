class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        nums_with_indices.sort()  # Sort by the number values
        
        left, right = 0, len(nums_with_indices) - 1
        
        while left < right:
            current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            if current_sum == target:
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

