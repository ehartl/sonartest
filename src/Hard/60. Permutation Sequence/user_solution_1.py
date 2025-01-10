class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(next(dropwhile(lambda t: t[0] < k, enumerate(permutations(list("123456789"[0:n])))))[1])
