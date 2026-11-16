class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement not in tracker:
                tracker[number] = index
            else:
                return ([tracker[complement], index])
    
