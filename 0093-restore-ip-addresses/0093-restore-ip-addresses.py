class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(index, parts):
            # If we have 4 parts
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            # Try 1, 2, or 3 digits
            for length in range(1, 4):

                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == '0':
                    continue

                # Value must be <= 255
                if int(part) > 255:
                    continue

                parts.append(part)

                backtrack(index + length, parts)

                parts.pop()

        # An IP address contains exactly 4 parts
        if 4 <= len(s) <= 12:
            backtrack(0, [])

        return result