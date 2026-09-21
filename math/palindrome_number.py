"""
Problem: Palindrome Number
LeetCode: #9
Difficulty: Easy
Pattern: Math

Time Complexity: O(log10(n))
Space Complexity: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes.
        # Numbers ending in 0 (except 0 itself) cannot be palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even-length numbers: x == reversed_half
        # For odd-length numbers: x == reversed_half // 10 (middle digit discarded)
        return x == reversed_half or x == reversed_half // 10
