"""
Problem: Roman to Integer
LeetCode: #13
Difficulty: Easy
Pattern: Hash Map / String Traversal

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        prev_value = 0

        # Traverse backwards to naturally handle subtraction cases (e.g. IV = 4, IX = 9)
        for char in reversed(s):
            curr_value = roman_values[char]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
                prev_value = curr_value

        return total
