class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for c in s:
            s_dict[c] = 1 + s_dict.get(c, 0)
        for c in t:
            if c in s_dict and s_dict[c] > 0:
                s_dict[c] -= 1
            else:
                return False
        return sum(s_dict.values()) == 0
        