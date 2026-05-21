class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        triples = []
        for i in range(len(nums)):
            if (i + 2 >= len(nums)):
                continue
            
            l, r = i + 1, len(sort) - 1
            while l < r:
                sum = sort[i] + sort[l] + sort[r]
                if sum == 0:
                    if ([sort[i], sort[l], sort[r]] not in triples):
                        triples.append([sort[i], sort[l], sort[r]])
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return triples