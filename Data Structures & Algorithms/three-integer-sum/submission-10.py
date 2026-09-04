class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets: List[List[int]] = []
        #[-40,-30,-4,-3,-1,-1,0,1,2,7,50,200,500]

        for index in range(len(nums) - 2):
            value = nums[index]
           
            if index > 0 and value == nums[index - 1]:
                continue

            if value > 0:
                break
            
            a = index + 1
            b = len(nums) - 1

            while a < b:          
                suma = value + nums[a] + nums[b]
                if suma == 0:
                    triplets.append([value, nums[a], nums[b]])
                    a += 1
                    b -= 1

                    while a < b and nums[a] == nums[a - 1]:
                        a += 1

                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1

                elif suma > 0: 
                    b -= 1
                else:
                    a += 1
                   
        return triplets
