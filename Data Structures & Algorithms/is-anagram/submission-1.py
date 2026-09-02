class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen1, seen2 = {}, {}
        for index, value in enumerate(s):
            seen1[value] = seen1.get(value, 0) + 1
            value_t = t[index]
            seen2[value_t] = seen2.get(value_t, 0) + 1
        return seen1 == seen2
