class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp ={}
        dp[1] = ["()"]
        dp[2] = ["(())","()()"]
        for i in range(3,n+1):
            d = {}
            arr = []
            for st in dp[i-1]:
                for j in range(0,len(st)):
                    new = st[0:j]+"()"+st[j:len(st)]
                    if new not in d:
                        d[new] = 1
                        arr.append(new)
            dp[i] = arr
        # print(dp[n])
        return dp[n]

