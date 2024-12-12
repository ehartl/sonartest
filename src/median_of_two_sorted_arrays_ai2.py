def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    length = len(merged)

    if length % 2 == 1:
        return float(merged[length // 2])
    else:
        return (merged[length // 2 - 1] + merged[length // 2]) / 2.0

# Example usage
print(findMedianSortedArrays([1, 3], [2]))  # Output: 2.00000
print(findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.50000