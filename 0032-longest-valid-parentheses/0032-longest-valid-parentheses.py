class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # Start a new valid substring
                    stack.append(i)
                else:
                    # Calculate current valid length
                    max_length = max(max_length, i - stack[-1])

        return max_length