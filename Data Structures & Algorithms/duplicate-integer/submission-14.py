class Solution:
    def hasDuplicate (self, nums):
        tracker = set()
        for number in nums:
            if number not in tracker:
                tracker.add(number)
            else:
                return True
        return False