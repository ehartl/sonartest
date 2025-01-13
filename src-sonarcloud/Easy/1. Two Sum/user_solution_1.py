class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for x in range(i + 1, len(nums)):
                if nums[i] + nums[x] == target:
                    return [i, x]
        return []
