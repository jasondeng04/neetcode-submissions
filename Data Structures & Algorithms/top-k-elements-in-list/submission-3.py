class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for number in nums:
            if number not in tracker:
                tracker[number] = 1
            else:
                tracker[number] += 1
        sorted_tracker = sorted(tracker.keys(), key= lambda number: tracker[number], reverse=True)
        return sorted_tracker[:k]



