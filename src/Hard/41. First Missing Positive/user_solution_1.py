class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Sorting positive numbers according to their space E.g [1,2,3,4]
        index = 0
        while index < len(nums):
            # Already in the place
            if index + 1 == nums[index]:    
                index += 1
            # No-use
            elif nums[index] <= 0:       
                  index += 1
            # No-use
            elif nums[index] > len(nums):  
                   index += 1
            # Already swapped
            elif nums[index] == nums[nums[index]-1]:
                index += 1
            else:
                A,B = index,nums[index]-1
                nums[A], nums[B] = nums[B], nums[A]
                
        #Smallest no which does not follow the true space
        for index in range(len(nums)):
            if index + 1 != nums[index]:   
                return index + 1
        # Otherwise, return the next positive number
        return len(nums) + 1
