from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the value and its index
        num_to_index = {}

        # Iterate over the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the two numbers
                return [num_to_index[complement], index]

            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index

        # If no solution is found, return an empty list (though the problem guarantees one solution)
        return []