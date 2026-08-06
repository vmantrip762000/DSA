class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while len(stack) > 0 and stack[-1][1] > h:
                Index, height = stack.pop()
                area = height * (i - Index)
                maxArea = max(maxArea, area)
                start = Index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
        