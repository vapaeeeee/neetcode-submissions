class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = self.findMinIndex(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            real_mid = self.realIndex(nums, mid, offset)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
            
    def realIndex(self, nums: List[int], virtual_index: int, offset: int) -> int:
        return (virtual_index + offset) % len(nums)

    def findMinIndex(self, nums: List[int]) -> int:
        minimum = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if mid > 0 and nums[mid - 1] > nums[mid]:
                minimum = mid
                break
            elif mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                minimum = mid + 1
                break
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid - 1

        return minimum