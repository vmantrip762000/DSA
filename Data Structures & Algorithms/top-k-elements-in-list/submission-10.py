class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = [[] for i in range(len(nums) + 1)]
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        # In count dictionary: key is a number and value is the frequency of number
        for i in count:
            freq_arr[count[i]].append(i)
        result = []
        for i in range(len(freq_arr) - 1, -1, -1):
            for j in freq_arr[i]:
                result.append(j)
                if len(result) == k:
                    return result

        