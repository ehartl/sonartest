class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        left, right = 0, abs(dividend)
        quotient = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * divisor <= dividend:
                quotient = mid
                left = mid + 1
            else:
                right = mid - 1

        if negative:
            quotient = -quotient

        return min(max(quotient, INT_MIN), INT_MAX)