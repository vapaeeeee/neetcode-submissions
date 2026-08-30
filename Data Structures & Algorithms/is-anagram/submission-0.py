class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen1 = {}
        seen2 = {}
        for index, value in enumerate(s):
            if value not in seen1:
                seen1[value] = 1
            else:
                seen1[value] += 1

            value_t = t[index]

            if value_t not in seen2:
                seen2[value_t] = 1
            else:
                seen2[value_t] += 1
        return seen1 == seen2
