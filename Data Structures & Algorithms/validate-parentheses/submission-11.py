class Solution:
    def isValid(self, s: str) -> bool:
        braces_dict = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in braces_dict:
                stack.append(c)
            elif len(stack) > 0 and c == braces_dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        