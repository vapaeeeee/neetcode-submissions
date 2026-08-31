class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            char_arr = [0] * 26

            for character in s:
                repr_num = ord(character) - ord("a")
                char_arr[repr_num] += 1
            
            key = tuple(char_arr)

            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)

        return list(groups.values())