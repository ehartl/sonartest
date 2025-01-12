class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        # Convert the number to a string
        str_x = str(x)
        left, right = 0, len(str_x) - 1
        
        while left < right:
            # Compare characters from both ends
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        
        return True

