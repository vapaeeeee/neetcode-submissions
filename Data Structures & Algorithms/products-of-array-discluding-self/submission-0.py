class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        cumulative = 1
        for key, value in enumerate(nums):
            prefixes[key] = cumulative
            cumulative *= value
        cumulative = 1
        for key, value in zip(range(len(nums) - 1, -1, -1), reversed(nums)):
            suffixes[key] = cumulative
            cumulative *= value
        return [a * b for a, b in zip(prefixes, suffixes)]