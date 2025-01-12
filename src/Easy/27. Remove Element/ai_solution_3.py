class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered_nums = [num for num in nums if num != val]
        nums[:len(filtered_nums)] = filtered_nums
        return len(filtered_nums)