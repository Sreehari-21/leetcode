# =========================
# LeetCode #13 - Roman to Integer
# =========================

class Solution:
    def romanToInt(self, s):

        # Store the value of each Roman symbol
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Store the final answer
        total = 0

        # Go through every character
        for i in range(len(s)):

            # Get the current value
            current = values[s[i]]

            # Check if there is a next character
            if i + 1 < len(s):

                # Get the next value
                next_value = values[s[i + 1]]

            # If this is the last character
            else:

                # There is no next value
                next_value = 0

            # If current is smaller than next
            if current < next_value:

                # Subtract current
                total -= current

            # Otherwise
            else:

                # Add current
                total += current

        # Return the final answer
        return total
