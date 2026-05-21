class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []
        for i in range(len(sortedNums) - 2):
            triplet = []
            anchor = i
            l = anchor + 1
            r = len(sortedNums) - 1

            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                    continue
            while l < r:
                threeSum = sortedNums[anchor] + sortedNums[l] + sortedNums[r]
                if threeSum == 0:
                    # save triplet
                    res.append([sortedNums[anchor], sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1
                    while l < r and sortedNums[r] == sortedNums[r + 1]:
                        r -= 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        return res


