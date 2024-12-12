class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.Median(nums1, nums2)

    def Median(self, nums1, nums2):
        i = 0
        j = 0
        count = 0
        flag = 0
        m1 = m2 = 0
        size = len(nums1) + len(nums2)
        while (count < size // 2 + 1):
            m2 = m1
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
            elif i < len(nums1):
                m1 = nums1[i]
                i += 1
            elif j < len(nums2):
                m1 = nums2[j]
                j += 1
            count += 1

        if size % 2 == 0:
            return (m1 + m2) / 2
        else:
            return m1

