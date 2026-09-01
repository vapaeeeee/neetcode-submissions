class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, frequency in counts.items():
            buckets[frequency].append(number)

        res = []

        for frequency in range(len(buckets) - 1, 0 , -1):
            for num in buckets[frequency]:
                res.append(num)
                if len(res) == k:
                    return res