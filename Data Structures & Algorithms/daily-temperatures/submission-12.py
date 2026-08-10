class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair = [temp, index]
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < t:
                temp, Index = stack.pop()
                res[Index] = i - Index
            stack.append([t, i])
        return res
        