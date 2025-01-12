class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def computeLPSArray(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        if not needle:
            return 0

        lps = computeLPSArray(needle)
        i = j = 0
        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == len(needle):
                return i - j
            elif i < len(haystack) and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1