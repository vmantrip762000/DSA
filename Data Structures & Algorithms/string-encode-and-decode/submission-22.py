class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        print(encode)
        return encode 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            #print(i)
            while s[j] != "#":
                j += 1
                print(j)
            length = int(s[i:j])
            res.append(s[j + 1 : j + length + 1])
            i = j + length + 1
        return res

