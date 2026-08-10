class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True

        for i, ch in enumerate(s):

            if ch.isdigit():
                seen_digit = True

                if seen_exp:
                    digit_after_exp = True

            elif ch == '.':
                # Dot is not allowed after exponent
                if seen_dot or seen_exp:
                    return False

                seen_dot = True

            elif ch == 'e' or ch == 'E':
                # Exponent needs digits before it
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                digit_after_exp = False

            elif ch == '+' or ch == '-':
                # Sign is allowed only at beginning
                # or immediately after e/E
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            else:
                return False

        return seen_digit and digit_after_exp