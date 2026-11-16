class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        running = 1
        best = 1
        sort_list = sorted(set(nums))
        if not sort_list:
            return 0
        previous = sort_list[0]
        for number in sort_list[1:]:
            difference = number - previous
            if difference == 1:
                running += 1
            else:
                running = 1
            previous = number
            best = max(running, best)
        return best
        