class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i in count:
            freq_arr[count[i]].append(i)
        res = []
        for i in range(len(freq_arr) - 1, -1, -1):
            for j in freq_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
        