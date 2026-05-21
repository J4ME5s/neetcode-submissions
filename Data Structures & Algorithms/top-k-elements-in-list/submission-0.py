class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        mostCommon = freqMap.most_common(k)

        return [num for num, count in mostCommon]