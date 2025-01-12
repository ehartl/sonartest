from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def commonPrefix(left: str, right: str) -> str:
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        def longestCommonPrefixRec(strs: List[str], l: int, r: int) -> str:
            if l == r:
                return strs[l]
            else:
                mid = (l + r) // 2
                lcpLeft = longestCommonPrefixRec(strs, l, mid)
                lcpRight = longestCommonPrefixRec(strs, mid + 1, r)
                return commonPrefix(lcpLeft, lcpRight)

        return longestCommonPrefixRec(strs, 0, len(strs) - 1)