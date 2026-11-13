class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        longest = 0
        l = 0
        for r, val in enumerate(s):
            while s[r] in window:
                del window[s[l]]
                l += 1
            window[val] = True
            longest = max(longest, r - l + 1)
        return longest

            
