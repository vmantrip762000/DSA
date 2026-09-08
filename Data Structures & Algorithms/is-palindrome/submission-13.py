class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            return ((ord('a') <= ord(c) <= ord('z')) or
                    (ord('A') <= ord(c) <= ord('Z')) or
                    (ord('0') <= ord(c) <= ord('9')))
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            if isAlphaNum(s[p1]) == True and isAlphaNum(s[p2]) == False:
                p2 -= 1
            elif isAlphaNum(s[p1]) == False and isAlphaNum(s[p2]) == True:
                p1 += 1
            elif isAlphaNum(s[p1]) == False and isAlphaNum(s[p2]) == False:
                p1 += 1
                p2 -= 1
            elif s[p1].lower() == s[p2].lower():
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
                
        