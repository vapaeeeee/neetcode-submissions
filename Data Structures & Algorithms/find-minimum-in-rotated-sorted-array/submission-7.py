class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if mid > 0 and nums[mid - 1] > nums[mid]:
                minimum = nums[mid]
                break
            elif mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                minimum = nums[mid + 1]
                break
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid - 1

        return minimum