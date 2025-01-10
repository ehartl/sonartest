class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.usingSortingAndTwoPointer(nums)
    
    def usingSortingAndTwoPointer(self, nums):
        nums.sort()
        added = set()
        out = []
        for i in range(len(nums) - 1, -1, -1):
            last = nums[i]
            start, end = 0, i - 1
            while start < end:
                s = last + nums[start] + nums[end]
                if s == 0:
                    if (last, nums[start], nums[end]) not in added: out.append([last, nums[start], nums[end]])
                    added.add((last, nums[start], nums[end]))
                    start += 1
                elif s > 0:
                    end -= 1
                else: start += 1
        return out
        
    
    #TLE, time complexity - o(n^3)
    def bruteForce(self, nums):
        out = []
        nums.sort()
        added = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0 and (a, b, c) not in added:
                        out.append([a, b, c])
                        added.add((a, b, c))
        return out
