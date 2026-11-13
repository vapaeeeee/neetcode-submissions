class Solution:
    def findMin(self, nums: List[int]) -> int:

        #nums = [3,4,5,6,1,2]
        
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid = (right - left) // 2
        #     if nums[mid] == target:
        #         return target
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else: 
        #         right = mid - 1

        minimum = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            print(mid)
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