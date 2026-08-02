class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            s_dict[tuple(count)].append(s)
        return list(s_dict.values())
            
        