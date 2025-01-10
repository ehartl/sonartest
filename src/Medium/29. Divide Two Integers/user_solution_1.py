class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 1: #not necessary but makes things simpler
            return dividend
        if dividend == -2**31 and divisor == -1: #accurately deal with overflow
            return 2**31-1
        neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        endres = 0
        while dividend >= divisor:
		   #At each iteration subtract the largest possible divisor*r=divisor*(2**k)
            resm = divisor
            r = 1
            while resm + resm < dividend:
                r += r
                resm += resm
            dividend -= resm
            endres += r
        return 0 - endres if neg else endres
