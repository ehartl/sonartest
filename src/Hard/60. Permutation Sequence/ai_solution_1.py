class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        k -= 1
        numbers = list(range(1, n + 1))
        result = []

        for i in range(1, n + 1):
            index = k // factorial[n - i]
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= factorial[n - i]

        return ''.join(result)