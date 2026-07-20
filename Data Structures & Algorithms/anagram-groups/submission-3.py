class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = defaultdict(list)
        for s in strs:
            str_arr = [0] * 26
            for c in s:
                str_arr[ord(c) - ord('a')] += 1
            word_dict[tuple(str_arr)].append(s)
        return list(word_dict.values())
            
        
        


        