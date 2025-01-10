class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
		n = len(s)
        if n < 2: return s
        dp, ans = [[0]*n for _ in range(n)], {}
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans[j-i+1] = s[i:j+1]
                else:
                    dp[i][j] = False
        return ans[max(ans)]
