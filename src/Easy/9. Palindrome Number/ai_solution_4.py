class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        # Convert the number to a string
        str_x = str(x)
        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]

