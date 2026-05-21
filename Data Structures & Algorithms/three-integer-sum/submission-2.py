class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSort = sorted(nums)
        res = []
        for i in range(len(numsSort) - 2):
            # init j, k
            j = i + 1
            k = len(numsSort) - 1
            while j < k:
                if numsSort[i] + numsSort[j] + numsSort[k] == 0:
                    if ([numsSort[i], numsSort[j], numsSort[k]] not in res):
                        res.append([numsSort[i], numsSort[j], numsSort[k]])
                    j += 1
                    k -= 1
                elif numsSort[i] + numsSort[j] + numsSort[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res