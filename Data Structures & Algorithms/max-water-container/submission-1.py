class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxArea = 0
        while start < end:
            width = end - start
            currArea = min(heights[start], heights[end]) * width
            if currArea > maxArea: maxArea = currArea
            if min(heights[start], heights[end]) == heights[start]:
                start += 1
            else:
                end -= 1
        return maxArea
