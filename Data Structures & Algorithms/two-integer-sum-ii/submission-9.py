class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            sumVal = numbers[p1] + numbers[p2]
            if sumVal < target:
                p1 += 1
            elif sumVal > target:
                p2 -= 1
            else:
                return [p1 + 1, p2 + 1]

        