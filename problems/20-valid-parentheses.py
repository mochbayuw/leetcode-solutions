class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
