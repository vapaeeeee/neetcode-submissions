class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #"XYYX"

        window = {}
        max_window = 0
        l = 0

        for r, val in enumerate(s):
            window[val] = window.get(val, 0) + 1
            highest_count = max(window.values())
            size = r - l + 1
       
            while size - highest_count > k:
                window[s[l]] = window.get(s[l]) - 1
                l += 1
                highest_count = max(window.values())
                size -= 1
                     
            max_window = max(max_window, r - l + 1)

        return max_window
