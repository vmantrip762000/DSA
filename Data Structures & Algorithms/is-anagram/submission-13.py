class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            s_dict[i] =  1 + s_dict.get(i,0)
        for i in t:
            if i in s_dict and s_dict[i] > 0:
                s_dict[i] -= 1
            else:
                return False
        return sum(list(s_dict.values())) == 0 

        

        