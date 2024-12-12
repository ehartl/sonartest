class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)  # Handle small cases

        k = 2  # Start from the third position
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k