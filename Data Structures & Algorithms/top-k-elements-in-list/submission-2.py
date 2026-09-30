class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            elif num in count:
                count[num] += 1
        final = sorted(count, key=lambda num: count[num], reverse=True)
        return final[:k]



