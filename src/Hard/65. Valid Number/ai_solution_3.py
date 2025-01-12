class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(s):
            if not s:
                return False
            if s[0] in '+-':
                s = s[1:]
            return s.isdigit()

        def is_decimal(s):
            if not s:
                return False
            if s[0] in '+-':
                s = s[1:]
            if '.' not in s:
                return s.isdigit()
            left, right = s.split('.', 1)
            if not left and not right:
                return False
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            return True

        def is_exponent(s):
            if 'e' in s:
                base, exp = s.split('e', 1)
            elif 'E' in s:
                base, exp = s.split('E', 1)
            else:
                return False
            return (is_integer(base) or is_decimal(base)) and is_integer(exp)

        s = s.strip()
        return is_integer(s) or is_decimal(s) or is_exponent(s)