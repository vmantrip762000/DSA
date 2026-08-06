class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "$" + s
        return encode

    def decode(self, s: str) -> List[str]:
        s_list = []
        i = 0
        while i <= len(s) - 1:
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            s_list.append(s[j+1:j+length+1])
            i = j + length + 1
        return s_list



