# =========================
# LeetCode #1 - Two Sum
# =========================

class Solution:
    def twoSum(self, nums, target):

        # Go through each number in the list
        for i in range(len(nums)):

            # Compare it with every number after it
            for j in range(i + 1, len(nums)):

                # Check if the two numbers add up to target
                if nums[i] + nums[j] == target:

                    # Return the indexes of the two numbers
                    return [i, j]
