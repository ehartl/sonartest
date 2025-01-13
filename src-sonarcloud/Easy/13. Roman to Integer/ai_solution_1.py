class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        stack = []
        for char in s:
            value = roman_to_int[char]
            if stack and stack[-1] < value:
                stack.append(value - stack.pop())
            else:
                stack.append(value)
        return sum(stack)