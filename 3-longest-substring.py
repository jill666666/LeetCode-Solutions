# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        start, end = 0, 1
        length_list = []
        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                length_list.append(len(s[start:end]))
                start += 1
                end = start + 1
        length_list.append(len(s[start:end]))
        print(length_list)
        return max(length_list)