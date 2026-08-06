class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        numSet = set(nums)
        for n in nums:
            if n-1 not in numSet:
                temp = 0
                while n+temp in numSet:
                    temp += 1
                    length = max(temp, length)
                    
                
                    
        return length
        