class Solution:
    def isValid(self, s: str) -> bool:
        stack, hm = [], {'(': ')', '{': '}', '[': ']'}
        for ch in s:
			# open bracket
            if ch in hm: 
                stack.append(ch)
			# close bracket
            else: 
                if not stack or hm[stack[-1]] != ch: return False
                stack.pop()

        return not stack
