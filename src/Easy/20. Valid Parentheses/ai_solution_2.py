class Solution:
    def isValid(self, s: str) -> bool:
        open_paren = open_brace = open_bracket = 0

        for char in s:
            if char == '(':
                open_paren += 1
            elif char == ')':
                open_paren -= 1
            elif char == '{':
                open_brace += 1
            elif char == '}':
                open_brace -= 1
            elif char == '[':
                open_bracket += 1
            elif char == ']':
                open_bracket -= 1

            if open_paren < 0 or open_brace < 0 or open_bracket < 0:
                return False

        return open_paren == open_brace == open_bracket == 0