class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        for i, a in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            k = len(nums) - 1
            j = i + 1
            while j < k:
                if a + nums[j] + nums[k] > 0:
                    k -= 1
                elif a + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                         j += 1
        return res


         