# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        temp = 0
        max_sum = nums[0]
        for i in range(0, len(nums)):
            temp = max(nums[i], nums[i] + temp)
            if temp > max_sum:
                max_sum = temp
        return max_sum