class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in tracker:
                tracker[sorted_word] = [word]
            else:
                tracker[sorted_word].append(word)
        return list(tracker.values())
