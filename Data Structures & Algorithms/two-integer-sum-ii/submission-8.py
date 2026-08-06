class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            trial = numbers[p1] + numbers[p2]
            if trial > target:
                p2 -= 1
            elif trial < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]
        