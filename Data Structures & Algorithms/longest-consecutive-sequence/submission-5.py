class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        numSet = set()
        for n in nums:
            if n - 1 not in numSet:
                temp = 0
                numSet.add(n)
                while n+temp in nums:
                    numSet.add(n+temp)
                    temp += 1
                    length = max(length, temp)
        return length
        
        