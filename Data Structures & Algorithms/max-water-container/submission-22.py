class Solution:

    def calc_area(self, heights: List[int], a: int, b: int) -> int:
        return (b-a) * min(heights[a], heights[b])

    # height=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        max_area = 0

        while a < b:
            area = self.calc_area(heights, a, b)
            if area > max_area:
                max_area = area
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1
            
        return max_area

    