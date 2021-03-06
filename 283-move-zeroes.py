# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

nums = [0, 1, 0, 3, 1, 2]
class Solution:
    def move_zeroes(nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1

    move_zeroes(nums)
