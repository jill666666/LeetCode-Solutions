# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return [item for item in counter if counter[item] % 2 == 1][0]