class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        leftMax = 0
        rightMax = 0
        res = 0
        while p1 <= p2:
            if leftMax <= rightMax:
                leftMax = max(leftMax, height[p1])
                res += leftMax - height[p1]
                p1 += 1
            else:
                rightMax = max(rightMax, height[p2])
                res += rightMax - height[p2]
                p2 -= 1
        return res

        