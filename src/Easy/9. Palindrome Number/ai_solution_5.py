class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        original = x
        reversed_num = 0
        
        while x > 0:
            # Extract the last digit
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            # Remove the last digit
            x //= 10
        
        # Check if the original number equals the reversed number
        return original == reversed_num

