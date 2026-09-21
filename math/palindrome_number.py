# =========================
# LeetCode #9 - Palindrome Number
# =========================

class Solution:
    def isPalindrome(self, x):

        # Convert the number into a string
        s = str(x)

        # Reverse the string and compare it with the original
        if s == s[::-1]:

            # If both are same, it is a palindrome
            return True

        # If both are different, it is not a palindrome
        else:
            return False