class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base Case
        if len(s) == 1: return 1


        count, s_result = 0, ''

        for i in s:
            if i not in s_result:
                s_result += i
            else:
                s_result = s_result[s_result.index(i)+1:] + i

            if len(s_result) > count:
                count = len(s_result)
        
        return count

            

            

            

        
