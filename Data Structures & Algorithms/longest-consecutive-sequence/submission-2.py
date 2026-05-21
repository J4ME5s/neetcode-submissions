class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valSet = set(nums)
        longest = 0
        for n in nums:
            consec = 0
            if (n - 1) not in valSet:
                # start streak
                consec += 1
                temp = n
                while temp + 1 in valSet:
                    consec += 1
                    temp += 1
                if consec > longest:
                    longest = consec
        
        return longest
