class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']

        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']

        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        dp[i].append(f'({left}){right}')

        return dp[n]