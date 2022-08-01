# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. 
# Otherwise, return -1.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

from cmath import pi
import re


class Solution():
    def search(self, nums, target):
        left, right = 0 , len(nums) - 1
        while left <= right:
            pivot = left + (right - left)  / 2 
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1 
            else:
                left = pivot + 1
        return -1


s = Solution()

print(s.search([-1,0,3,5,9,12],9))