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

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        if negative:
            quotient = -quotient

        return min(max(quotient, INT_MIN), INT_MAX)