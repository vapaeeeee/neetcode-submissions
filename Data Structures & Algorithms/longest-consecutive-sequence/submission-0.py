class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dik = {}
        for num in nums:
            dik[num] = num

        longest_sequence = 0

        for key in dik:
            if key - 1 in dik:
                continue

            curr_length = 1

            while key + curr_length in dik:
                curr_length += 1

            longest_sequence = max(longest_sequence, curr_length)

        return longest_sequence