# LeetCode 1: Two Sum
# Find two numbers whose sum equals the target.
# Use a dictionary to remember numbers we have already seen.
# If the required number is found, return the indices.

class Solution:
    def twoSum(self, nums, target):
        number = {} # Store numbers and their indices

        for i in range(len(nums)): # Go through each no. in the list 
            comp = target - nums[i] # Find the number needed to reach the target

            if comp in num:
                return [number[comp], i]
