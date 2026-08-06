class Solution:
    def isValid(self, s):
        stack = []
        
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != brackets[ch]:
                    return False

        return len(stack) == 0