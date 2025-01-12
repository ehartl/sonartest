class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            if i == len(s):
                return all(x == '*' for x in p[j:])

            if p[j] == '*':
                memo[(i, j)] = dfs(i, j + 1) or dfs(i + 1, j)
            else:
                memo[(i, j)] = (p[j] in {s[i], '?'}) and dfs(i + 1, j + 1)

            return memo[(i, j)]

        return dfs(0, 0)