class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = [-1] * 128
        left = 0
        max_length = 0

        for right in range(len(s)):
            if last_index[ord(s[right])] >= left:
                left = last_index[ord(s[right])] + 1
            last_index[ord(s[right])] = right
            max_length = max(max_length, right - left + 1)

        return max_length