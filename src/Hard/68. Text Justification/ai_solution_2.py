class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        breaks = [-1] * n

        for i in range(n - 1, -1, -1):
            length = -1
            for j in range(i, n):
                length += len(words[j]) + 1
                if length > maxWidth:
                    break
                cost = (maxWidth - length + 1) ** 2 + dp[j + 1]
                if cost < dp[i]:
                    dp[i] = cost
                    breaks[i] = j + 1

        result = []
        i = 0
        while i < n:
            j = breaks[i]
            line = ' '.join(words[i:j])
            if j < n:
                line += ' ' * (maxWidth - len(line))
            result.append(line)
            i = j

        return result