class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        triplets: List[List[int]] = []

        nums.sort()
        #[-40,-30,-4,-3,-1,-1,0,1,2,7,50,200,500]

        for index, value in enumerate(nums):
            if index <= len(nums):

                if index > 0 and value == nums[index - 1]:
                    continue

                if value > 0:
                    break
                
                a = index + 1
                b = len(nums) - 1

                while a < b:          
                    suma = value + nums[a] + nums[b]
                    triplet = [value, nums[a], nums[b]]
                    if suma == 0:
                        if triplet not in triplets:
                            triplets.append(triplet)
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
                   
        
        unique_list = [list(item) for item in set(tuple(i) for i in triplets)]
        return unique_list