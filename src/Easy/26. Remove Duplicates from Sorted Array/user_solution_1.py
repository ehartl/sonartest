def removeDuplicates(self, nums: List[int]) -> int:
        position = 1
        current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == current:
                continue
            current = nums[i]
            nums[i], nums[position] = nums[position], nums[i]
            position += 1

        return position
