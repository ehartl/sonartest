class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0
        
        while i < len(s):
            # Check if the current character and the next one form a subtraction case
            if i + 1 < len(s) and s[i:i+2] in {"IV", "IX", "XL", "XC", "CD", "CM"}:
                total += roman_map[s[i+1]] - roman_map[s[i]]
                i += 2  # Skip the next character
            else:
                total += roman_map[s[i]]
                i += 1
        
        return total

