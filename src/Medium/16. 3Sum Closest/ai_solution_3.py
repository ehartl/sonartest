class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                if complement in seen:
                    current_sum = nums[i] + nums[j] + complement
                    if abs(current_sum - target) < abs(closest_sum - target):
                        closest_sum = current_sum
                seen.add(nums[j])

        return closest_sum