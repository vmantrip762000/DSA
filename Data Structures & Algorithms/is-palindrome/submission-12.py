class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            return ((ord('0') <= ord(c) <= ord('9')) or
                    (ord('a') <= ord(c) <= ord('z')) or
                    ord('A') <= ord(c) <= ord('Z'))
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if not isAlphaNum(s[p1]):
                p1 += 1
            elif not isAlphaNum(s[p2]):
                p2 -= 1
            elif s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                p2 -= 1
        return True
            

        