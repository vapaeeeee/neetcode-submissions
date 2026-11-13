from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        tdict = dict(Counter(t))
        window = {}
        left = 0
        min_start = 0
        min_length = math.inf
        have, need = 0, len(tdict)

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in tdict and window[char] == tdict[char]:
                have += 1

            while have == need:
                length = right - left + 1
                if length < min_length:
                    min_length = length
                    min_start = left

                window[s[left]] -= 1
                if s[left] in tdict and window[s[left]] < tdict[s[left]]:
                    have -= 1
                left += 1

        if min_length == math.inf:
            min_length = 0

        return s[min_start:min_start + min_length]
