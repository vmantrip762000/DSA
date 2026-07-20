class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in s_dict:
                stack.append(c)
            elif len(stack) > 0 and c == s_dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0




        