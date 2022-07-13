# https://leetcode.com/problems/find-pivot-index/

# The pivot index is the index where the sum of all the numbers strictly to the left of the 
# index is equal to the sum of all the numbers strictly to the index's right.

# Example 1:
###########################################################
# Input: nums = [1,7,3,6,5,6]                             # 
# Output: 3                                               #
# Explanation:  3                                         #
# The pivot index is 3.                                   #
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 #
# Right sum = nums[4] + nums[5] = 5 + 6 = 11              #
###########################################################
class solution():
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            if leftSum == (rightSum - nums[i] - leftSum):
                return i
            leftSum += nums[i]
        return -1


s = solution()
print(
    s.pivotIndex([1, 7, 3, 6, 5, 6]))
